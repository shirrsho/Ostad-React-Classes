from django.contrib import admin
from .models import Category, Course, Lesson, Material, Enrollment, QuestionAnswer



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor_id', 'category_id', 'price', 'is_active', 'created_at')
    list_filter = ('category_id', 'is_active', 'created_at', 'instructor_id')
    search_fields = ('title', 'description', 'instructor_id__username')
    ordering = ('-created_at',)
    raw_id_fields = ('instructor_id',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('instructor_id', 'category_id')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_id', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'course_id')
    search_fields = ('title', 'description', 'course_id__title')
    ordering = ('-created_at',)
    raw_id_fields = ('course_id',)

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_id', 'file_type', 'is_active', 'created_at')
    list_filter = ('file_type', 'is_active', 'created_at', 'course_id')
    search_fields = ('title', 'description', 'course_id__title')
    ordering = ('-created_at',)
    raw_id_fields = ('course_id',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'course_id', 'progress', 'is_completed', 'is_certificate_ready', 'created_at')
    list_filter = ('is_completed', 'is_certificate_ready', 'created_at', 'course_id')
    search_fields = ('student_id__username', 'course_id__title')
    ordering = ('-created_at',)
    raw_id_fields = ('student_id', 'course_id')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('student_id', 'course_id')

@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'lesson_id', 'description_truncated', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at', 'lesson_id__course_id')
    search_fields = ('user_id__username', 'lesson_id__title', 'description')
    ordering = ('-created_at',)
    raw_id_fields = ('user_id', 'lesson_id')
    
    def description_truncated(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_truncated.short_description = 'Description'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user_id', 'lesson_id')