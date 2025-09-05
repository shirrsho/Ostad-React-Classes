from django.db import models
from users.models import User
import re

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.ImageField(upload_to='course_banners/')
    price = models.FloatField()
    duration = models.FloatField()
    is_active = models.BooleanField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'teacher'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    LESSON_TYPES = [
        ('youtube', 'YouTube Video'),
        ('upload', 'Uploaded Video'),
        ('text', 'Text Content'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    lesson_type = models.CharField(max_length=20, choices=LESSON_TYPES, default='youtube')
    
    # For YouTube videos
    youtube_url = models.URLField(blank=True, null=True, help_text="YouTube video URL")
    
    # For uploaded videos (existing field)
    video = models.FileField(upload_to='lesson_videos', blank=True, null=True)
    
    # For text content
    text_content = models.TextField(blank=True, null=True)
    
    # Lesson ordering
    order = models.PositiveIntegerField(default=0)
    
    # Duration in minutes
    duration_minutes = models.PositiveIntegerField(default=0, help_text="Duration in minutes")
    
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title
    
    def get_youtube_embed_url(self):
        """Convert YouTube URL to embed URL"""
        if not self.youtube_url:
            return None
        
        # Extract video ID from various YouTube URL formats
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.youtube_url)
            if match:
                video_id = match.group(1)
                return f"https://www.youtube.com/embed/{video_id}"
        
        return None
    
    def get_youtube_thumbnail(self):
        """Get YouTube video thumbnail"""
        if not self.youtube_url:
            return None
        
        patterns = [
            r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
            r'youtube\.com/embed/([a-zA-Z0-9_-]{11})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, self.youtube_url)
            if match:
                video_id = match.group(1)
                return f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        
        return None

class LessonProgress(models.Model):
    """Track student progress for each lesson"""
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    watch_time_seconds = models.PositiveIntegerField(default=0)  # Track how much was watched
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['student', 'lesson']
    
    def __str__(self):
        return f"{self.student.username} - {self.lesson.title} - {'Completed' if self.is_completed else 'In Progress'}"

class Material(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file_type = models.CharField(max_length=100)
    file = models.FileField(upload_to='materials/')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role' : 'student'})
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    price = models.FloatField()
    progress = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    total_mark = models.FloatField(default=0)
    is_certificate_ready = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student_id.username} - {self.course_id.title}"
    
    def calculate_progress(self):
        """Calculate progress based on completed lessons"""
        total_lessons = self.course_id.lesson_set.filter(is_active=True).count() # total lesson = 10
        if total_lessons == 0:
            return 0
        
        completed_lessons = LessonProgress.objects.filter(
            student=self.student_id,
            lesson__course_id=self.course_id,
            is_completed=True
        ).count() # total Completed lessons = 5
        
        progress = int((completed_lessons / total_lessons) * 100) # (5/10)*100 = 50%
        
        # Update progress and completion status
        self.progress = progress
        self.is_completed = progress == 100
        self.save()
        
        return progress

class QuestionAnswer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_id.username} --> {self.lesson_id.title} --> {self.description}"