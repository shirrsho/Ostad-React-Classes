from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from core.models import Course, Category, Enrollment
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model

User = get_user_model()

@csrf_protect
def signup_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard') # url name dashboard
        return render(request, 'users/signup.html')

    elif request.method == 'POST':
        first_name = request.POST.get('first_name')    
        last_name = request.POST.get('last_name')    
        email = request.POST.get('email')    
        username = request.POST.get('username')  
        password = request.POST.get('password')    
        password_confirm = request.POST.get('password_confirm')    
        role = request.POST.get('role') 

        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'users/signup.html')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'users/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'users/signup.html')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            role=role
        )
        login(request, user)
        return redirect('dashboard')
        
          
@csrf_protect
def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dashboard') # url name dashboard
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or Password')
            return render(request, 'users/login.html')
        

@login_required
def dashboard_view(request):
    user = request.user
    context = {'user' : user}

    if user.role == 'teacher':
        teacher_courses = Course.objects.filter(instructor_id=user)
        total_students = Enrollment.objects.filter(course_id__instructor_id=user).count()
        context.update({
            'courses' : teacher_courses,
            'total_courses' : teacher_courses.count(),
            'total_students' : total_students,
            'total_hours' : sum([course.duration for course in teacher_courses])
        })
        return render(request, 'users/teacher_dashboard.html', context)
    else: # student
        enrollments = Enrollment.objects.filter(student_id = user)
        completed_course = enrollments.filter(is_completed = True).count()
        context.update({
            'enrollments' : enrollments,
            'total_enrolled' : enrollments.count(),
            'completed_course' : completed_course,
            'certificate_earned' : enrollments.filter(is_certificate_ready = True).count(),
            'total_hours' : sum([e.course_id.duration for e in enrollments if e.is_completed])
        })
        return render(request, 'users/student_dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    featured_courses = Course.objects.filter(is_active = True)
    categories = Category.objects.filter(is_active = True)

    context = {
        'featured_courses' : featured_courses,
        'categories' : categories,
        'total_courses' : featured_courses.count(),
        'total_students' : User.objects.filter(role='student').count(),
        'total_teachers' : User.objects.filter(role='teacher').count(),
    }
    return render(request, 'index.html', context)