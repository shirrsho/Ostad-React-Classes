from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.utils import timezone
from .models import Course, Category, Lesson, Material, Enrollment, QuestionAnswer, LessonProgress
from users.models import User
import json

# ===============================
# PUBLIC COURSE VIEWS
# ===============================

def courses_list_view(request):
    """Public course listing with search, filter, and pagination"""
    courses = Course.objects.filter(is_active=True).select_related('instructor_id', 'category_id')
    categories = Category.objects.filter(is_active=True)
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        courses = courses.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(instructor_id__first_name__icontains=search) |
            Q(instructor_id__last_name__icontains=search)
        )
    
    # Category filter
    category_filter = request.GET.get('category')
    if category_filter:
        courses = courses.filter(category_id__id=category_filter)
    
    # Price filter
    price_filter = request.GET.get('price')
    if price_filter == 'free':
        courses = courses.filter(price=0)
    elif price_filter == 'paid':
        courses = courses.filter(price__gt=0)
    
    # Sort functionality
    sort_by = request.GET.get('sort', 'popular')
    if sort_by == 'newest':
        courses = courses.order_by('-created_at')
    elif sort_by == 'price_low':
        courses = courses.order_by('price')
    elif sort_by == 'price_high':
        courses = courses.order_by('-price')
    else:  # popular
        courses = courses.annotate(
            enrollment_count=Count('enrollment')
        ).order_by('-enrollment_count')
    
    paginator = Paginator(courses, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'courses': page_obj,
        'categories': categories,
        'search': search,
        'category_filter': category_filter,
        'price_filter': price_filter,
        'sort_by': sort_by,
    }
    return render(request, 'courses/courses_list.html', context)

def course_detail_view(request, course_id):
    """Public course detail page"""
    course = get_object_or_404(Course, id=course_id, is_active=True)
    lessons = Lesson.objects.filter(course_id=course, is_active=True).order_by('order', 'created_at')
    materials = Material.objects.filter(course_id=course, is_active=True).order_by('created_at')
    
    # Check if user is enrolled
    is_enrolled = False
    enrollment = None
    if request.user.is_authenticated:
        try:
            enrollment = Enrollment.objects.get(student_id=request.user, course_id=course)
            is_enrolled = True
        except Enrollment.DoesNotExist:
            pass
    
    # Get course statistics
    total_enrollments = Enrollment.objects.filter(course_id=course).count()
    
    # Related courses
    related_courses = Course.objects.filter(
        category_id=course.category_id,
        is_active=True
    ).exclude(id=course.id)[:3]
    
    context = {
        'course': course,
        'lessons': lessons,
        'materials': materials,
        'is_enrolled': is_enrolled,
        'enrollment': enrollment,
        'total_enrollments': total_enrollments,
        'related_courses': related_courses,
    }
    return render(request, 'courses/course_detail.html', context)

@login_required
def enroll_course_view(request, course_id):
    """Handle course enrollment"""
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id, is_active=True)
        
        # Check if already enrolled
        if Enrollment.objects.filter(student_id=request.user, course_id=course).exists():
            messages.warning(request, 'You are already enrolled in this course.')
            return redirect('course_detail', course_id=course_id)
        
        # Create enrollment
        enrollment = Enrollment.objects.create(
            student_id=request.user,
            course_id=course,
            price=course.price
        )
        
        messages.success(request, f'Successfully enrolled in {course.title}!')
        return redirect('course_detail', course_id=course_id)
    
    return redirect('courses_list')

# ===============================
# STUDENT LESSON VIEWS
# ===============================

@login_required
def lesson_detail_view(request, course_id, lesson_id):
    """View individual lesson - only for enrolled students"""
    course = get_object_or_404(Course, id=course_id, is_active=True)
    lesson = get_object_or_404(Lesson, id=lesson_id, course_id=course, is_active=True)
    
    # Check if user is enrolled
    try:
        enrollment = Enrollment.objects.get(student_id=request.user, course_id=course)
    except Enrollment.DoesNotExist:
        messages.error(request, 'You need to enroll in this course to access lessons.')
        return redirect('course_detail', course_id=course_id)
    
    # Get or create lesson progress
    lesson_progress, created = LessonProgress.objects.get_or_create(
        student=request.user,
        lesson=lesson,
        defaults={'is_completed': False}
    )
    
    # Get all lessons in the course for navigation
    all_lessons = Lesson.objects.filter(course_id=course, is_active=True).order_by('order', 'created_at')
    
    # Get previous and next lessons
    lesson_list = list(all_lessons)
    current_index = lesson_list.index(lesson)
    
    previous_lesson = lesson_list[current_index - 1] if current_index > 0 else None
    next_lesson = lesson_list[current_index + 1] if current_index < len(lesson_list) - 1 else None
    
    # Get questions for this lesson
    questions = QuestionAnswer.objects.filter(
        lesson_id=lesson,
        is_active=True
    ).select_related('user_id').order_by('-created_at')
    
    context = {
        'course': course,
        'lesson': lesson,
        'lesson_progress': lesson_progress,
        'all_lessons': all_lessons,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
        'questions': questions,
        'enrollment': enrollment,
    }
    
    return render(request, 'courses/lesson_detail.html', context)

@login_required
@csrf_exempt
def mark_lesson_complete(request):
    """Mark a lesson as complete (MVT version, no AJAX/JSON)"""
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        watch_time = int(request.POST.get('watch_time', 0))

        lesson = get_object_or_404(Lesson, id=lesson_id)

        # Check enrollment
        enrollment = Enrollment.objects.filter(
            student_id=request.user,
            course_id=lesson.course_id
        ).first()

        if not enrollment:
            messages.error(request, 'You are not enrolled in this course.')
            return redirect('course_detail', course_id=lesson.course_id)

        # Update lesson progress
        lesson_progress, created = LessonProgress.objects.get_or_create(
            student_id=request.user,
            lesson=lesson,
            defaults={
                'is_completed': True,
                'watch_time_seconds': watch_time,
                'completed_at': timezone.now()
            }
        )

        if not lesson_progress.is_completed:
            lesson_progress.is_completed = True
            lesson_progress.watch_time_seconds = watch_time
            lesson_progress.completed_at = timezone.now()
            lesson_progress.save()

        # Update overall progress (optional if shown on course page)
        new_progress = enrollment.calculate_progress()

        messages.success(request, 'Lesson marked as complete!')
        return redirect('lesson_detail',course_id = lesson.course_id.id, lesson_id=lesson.id)

    messages.error(request, 'Invalid request method.')
    return redirect('home')
# ===============================
# QUESTION & ANSWER VIEWS
# ===============================

@login_required
def course_questions_view(request, course_id):
    """View questions for a course"""
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course_id=course, is_active=True)
    
    questions = QuestionAnswer.objects.filter(
        lesson_id__course_id=course,
        is_active=True
    ).select_related('user_id', 'lesson_id').order_by('-created_at')
    
    # Filter by lesson
    lesson_filter = request.GET.get('lesson')
    if lesson_filter:
        questions = questions.filter(lesson_id__id=lesson_filter)
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        questions = questions.filter(
            Q(description__icontains=search) |
            Q(user_id__first_name__icontains=search) |
            Q(user_id__last_name__icontains=search)
        )
    
    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'course': course,
        'lessons': lessons,
        'questions': page_obj,
        'lesson_filter': lesson_filter,
        'search': search,
    }
    return render(request, 'courses/course_questions.html', context)

@login_required
@csrf_exempt
def create_question_view(request):
    """Create a new question (standard POST, no JSON)"""
    if request.method == 'POST':
        lesson_id = request.POST.get('lesson_id')
        description = request.POST.get('description')

        lesson = get_object_or_404(Lesson, id=lesson_id)

        QuestionAnswer.objects.create(
            user_id=request.user,
            lesson_id=lesson,
            description=description,
            is_active=True
        )

        messages.success(request, 'Question posted successfully!')
        return redirect('lesson_detail', course_id=lesson.course_id.id, lesson_id=lesson.id)

    messages.error(request, 'Invalid request method.')
    return redirect('home')
# ===============================
# TEACHER VIEWS
# ===============================

@login_required
def teacher_courses_view(request):
    """Teacher's course management dashboard"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    courses = Course.objects.filter(instructor_id=request.user).order_by('-created_at')
    
    context = {
        'courses': courses,
    }
    return render(request, 'courses/teacher_courses.html', context)

@login_required
def teacher_create_course_view(request):
    """Create new course"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        banner = request.FILES.get('banner')
        price_str = request.POST.get('price', '0').strip()
        duration_str = request.POST.get('duration', '0').strip()
        
        # Convert safely, fallback to 0 if empty or invalid
        try:
            price = float(price_str) if price_str else 0.0
        except (ValueError, TypeError):
            price = 0.0
        
        try:
            duration = float(duration_str) if duration_str else 0.0
        except (ValueError, TypeError):
            duration = 0.0
            
        category = get_object_or_404(Category, id=category_id)
        
        course = Course.objects.create(
            title=title,
            description=description,
            category_id=category,
            instructor_id=request.user,
            price=price,
            duration=duration,
            banner=banner,
            is_active=True
        )
        
        messages.success(request, f'Course "{title}" created successfully!')
        return redirect('teacher_courses')
    
    categories = Category.objects.filter(is_active=True)
    context = {
        'categories': categories,
    }
    return render(request, 'courses/teacher_create_course.html', context)

@login_required
def teacher_edit_course_view(request, course_id):
    """Edit existing course"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    
    if request.method == 'POST':
        course.title = request.POST.get('title')
        course.description = request.POST.get('description')
        category_id = request.POST.get('category_id')
        course.category_id = get_object_or_404(Category, id=category_id)
        course.price = float(request.POST.get('price', 0))
        course.duration = float(request.POST.get('duration', 0))
        
        if request.FILES.get('banner'):
            course.banner = request.FILES.get('banner')
        
        course.save()
        
        messages.success(request, f'Course "{course.title}" updated successfully!')
        return redirect('teacher_courses')
    
    categories = Category.objects.filter(is_active=True)
    context = {
        'course': course,
        'categories': categories,
    }
    return render(request, 'courses/teacher_edit_course.html', context)

@login_required
def teacher_course_students_view(request, course_id):
    """View students enrolled in a course"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    enrollments = Enrollment.objects.filter(course_id=course).select_related('student_id').order_by('-created_at')
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        enrollments = enrollments.filter(
            Q(student_id__first_name__icontains=search) |
            Q(student_id__last_name__icontains=search) |
            Q(student_id__username__icontains=search) |
            Q(student_id__email__icontains=search)
        )
    
    # Progress filter
    progress_filter = request.GET.get('progress')
    if progress_filter == 'not_started':
        enrollments = enrollments.filter(progress=0)
    elif progress_filter == 'in_progress':
        enrollments = enrollments.filter(progress__gt=0, progress__lt=100)
    elif progress_filter == 'completed':
        enrollments = enrollments.filter(progress=100)
    
    paginator = Paginator(enrollments, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'course': course,
        'enrollments': page_obj,
        'search': search,
        'progress_filter': progress_filter,
    }
    return render(request, 'courses/teacher_course_students.html', context)

@login_required
def teacher_course_lessons_view(request, course_id):
    """View lessons for a course with statistics"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    lessons = Lesson.objects.filter(course_id=course).order_by('order', 'created_at')
    
    # Get lesson statistics
    lesson_stats = []
    for lesson in lessons:
        total_enrolled = Enrollment.objects.filter(course_id=course).count()
        completed_count = LessonProgress.objects.filter(
            lesson=lesson,
            is_completed=True
        ).count()
        
        completion_rate = (completed_count / total_enrolled * 100) if total_enrolled > 0 else 0
        
        lesson_stats.append({
            'lesson': lesson,
            'completed_count': completed_count,
            'total_enrolled': total_enrolled,
            'completion_rate': completion_rate
        })
    
    context = {
        'course': course,
        'lesson_stats': lesson_stats,
        'lessons': lessons,
    }
    return render(request, 'courses/teacher_course_lessons.html', context)

@login_required
def teacher_create_lesson_view(request, course_id):
    """Create new lesson with multiple content types"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        lesson_type = request.POST.get('lesson_type', 'youtube')
        duration_minutes = int(request.POST.get('duration_minutes', 0))
        order = int(request.POST.get('order', 0))
        
        # Create lesson based on type
        lesson = Lesson.objects.create(
            title=title,
            description=description,
            lesson_type=lesson_type,
            duration_minutes=duration_minutes,
            order=order,
            course_id=course,
            is_active=True
        )
        
        if lesson_type == 'youtube':
            youtube_url = request.POST.get('youtube_url')
            lesson.youtube_url = youtube_url
            lesson.save()
        elif lesson_type == 'upload':
            video = request.FILES.get('video')
            lesson.video = video
            lesson.save()
        elif lesson_type == 'text':
            text_content = request.POST.get('text_content')
            lesson.text_content = text_content
            lesson.save()
        
        messages.success(request, f'Lesson "{title}" created successfully!')
        return redirect('teacher_course_lessons', course_id=course_id)
    
    # Get current lessons count for ordering
    lessons_count = Lesson.objects.filter(course_id=course).count()
    
    context = {
        'course': course,
        'lessons_count': lessons_count,
    }
    return render(request, 'courses/teacher_create_lesson.html', context)

@login_required
def teacher_edit_lesson_view(request, course_id, lesson_id):
    """Edit existing lesson"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    lesson = get_object_or_404(Lesson, id=lesson_id, course_id=course)
    
    if request.method == 'POST':
        lesson.title = request.POST.get('title')
        lesson.description = request.POST.get('description')
        lesson.lesson_type = request.POST.get('lesson_type', 'youtube')
        lesson.duration_minutes = int(request.POST.get('duration_minutes', 0))
        lesson.order = int(request.POST.get('order', 0))
        
        # Update content based on type
        if lesson.lesson_type == 'youtube':
            lesson.youtube_url = request.POST.get('youtube_url')
            lesson.video = None  # Clear uploaded video
            lesson.text_content = None  # Clear text content
        elif lesson.lesson_type == 'upload':
            video = request.FILES.get('video')
            if video:
                lesson.video = video
            lesson.youtube_url = None  # Clear YouTube URL
            lesson.text_content = None  # Clear text content
        elif lesson.lesson_type == 'text':
            lesson.text_content = request.POST.get('text_content')
            lesson.youtube_url = None  # Clear YouTube URL
            lesson.video = None  # Clear uploaded video
        
        lesson.save()
        
        messages.success(request, f'Lesson "{lesson.title}" updated successfully!')
        return redirect('teacher_course_lessons', course_id=course_id)
    
    context = {
        'course': course,
        'lesson': lesson,
    }
    return render(request, 'courses/teacher_edit_lesson.html', context)

@login_required
def teacher_course_materials_view(request, course_id):
    """View materials for a course"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    materials = Material.objects.filter(course_id=course).order_by('created_at')
    
    context = {
        'course': course,
        'materials': materials,
    }
    return render(request, 'courses/teacher_course_materials.html', context)

@login_required
def teacher_create_material_view(request, course_id):
    """Create new material"""
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    course = get_object_or_404(Course, id=course_id, instructor_id=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file_type = request.POST.get('file_type')
        file = request.FILES.get('file')
        
        material = Material.objects.create(
            title=title,
            description=description,
            file_type=file_type,
            file=file,
            course_id=course,
            is_active=True
        )
        
        messages.success(request, f'Material "{title}" created successfully!')
        return redirect('teacher_course_materials', course_id=course_id)
    
    context = {
        'course': course,
    }
    return render(request, 'courses/teacher_create_material.html', context)