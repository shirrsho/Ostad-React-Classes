from django.urls import path
from . import views

urlpatterns = [
    # Public course views
    path('', views.courses_list_view, name='courses_list'),
    path('<int:course_id>/', views.course_detail_view, name='course_detail'),
    path('<int:course_id>/enroll/', views.enroll_course_view, name='enroll_course'),
    path('<int:course_id>/questions/', views.course_questions_view, name='course_questions'),
    path('questions/create/', views.create_question_view, name='create_question'),
    
    # Lesson views
    path('<int:course_id>/lessons/<int:lesson_id>/', views.lesson_detail_view, name='lesson_detail'),
    path('lessons/complete/', views.mark_lesson_complete, name='mark_lesson_complete'),
    
    # Teacher URLs
    path('teacher/', views.teacher_courses_view, name='teacher_courses'),
    path('teacher/create/', views.teacher_create_course_view, name='teacher_create_course'),
    path('teacher/<int:course_id>/edit/', views.teacher_edit_course_view, name='teacher_edit_course'),
    path('teacher/<int:course_id>/students/', views.teacher_course_students_view, name='teacher_course_students'),
    path('teacher/<int:course_id>/lessons/', views.teacher_course_lessons_view, name='teacher_course_lessons'),
    path('teacher/<int:course_id>/lessons/create/', views.teacher_create_lesson_view, name='teacher_create_lesson'),
    path('teacher/<int:course_id>/lessons/<int:lesson_id>/edit/', views.teacher_edit_lesson_view, name='teacher_edit_lesson'),
    path('teacher/<int:course_id>/materials/', views.teacher_course_materials_view, name='teacher_course_materials'),
    path('teacher/<int:course_id>/materials/create/', views.teacher_create_material_view, name='teacher_create_material'),
    
]