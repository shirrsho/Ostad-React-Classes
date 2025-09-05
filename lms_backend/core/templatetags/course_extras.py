from django import template
from django.utils.safestring import mark_safe
from core.models import Enrollment


register = template.Library()

@register.filter
def is_enrolled(user, course):
    """Check if user is enrolled in course"""
    if not user.is_authenticated:
        return False
    return Enrollment.objects.filter(student_id=user, course_id=course).exists()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """
    Replace or add query parameters to the current request URL.
    Example: {% url_replace page=2 %}
    """
    query = context['request'].GET.copy()
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()

@register.filter
def enrollment_progress(user, course):
    """Get user's progress in course"""
    if not user.is_authenticated:
        return 0
    try:
        enrollment = Enrollment.objects.get(student_id=user, course_id=course)
        return enrollment.progress
    except Enrollment.DoesNotExist:
        return 0

@register.filter
def course_rating(course):
    """Calculate course rating (placeholder - implement with actual rating system)"""
    # This is a placeholder - you can implement actual rating calculation
    import random
    return round(random.uniform(3.5, 5.0), 1)

@register.filter
def format_duration(hours):
    """Format duration in hours to readable format"""
    if hours < 1:
        return f"{int(hours * 60)} minutes"
    elif hours < 24:
        return f"{int(hours)} hours"
    else:
        days = int(hours / 24)
        remaining_hours = int(hours % 24)
        if remaining_hours > 0:
            return f"{days} days, {remaining_hours} hours"
        return f"{days} days"

@register.filter
def format_price(price):
    """Format price for display"""
    if price == 0:
        return "Free"
    return f"${price:.2f}"

@register.inclusion_tag('courses/partials/course_card.html')
def course_card(course, user=None):
    """Render a course card with enrollment status"""
    context = {
        'course': course,
        'is_enrolled': False,
        'progress': 0,
    }
    
    if user and user.is_authenticated:
        try:
            enrollment = Enrollment.objects.get(student_id=user, course_id=course)
            context['is_enrolled'] = True
            context['progress'] = enrollment.progress
        except Enrollment.DoesNotExist:
            pass
    
    return context

@register.simple_tag
def progress_bar(percentage, show_text=True):
    """Generate a progress bar HTML"""
    html = f'''
    <div class="progress" style="height: 8px;">
        <div class="progress-bar" role="progressbar" 
             style="width: {percentage}%;" 
             aria-valuenow="{percentage}" 
             aria-valuemin="0" 
             aria-valuemax="100">
        </div>
    </div>
    '''
    
    if show_text:
        html += f'<small class="text-muted">{percentage}% complete</small>'
    
    return mark_safe(html)

@register.simple_tag
def user_avatar(user, size=40):
    """Generate user avatar HTML"""
    initials = f"{user.first_name[:1]}{user.last_name[:1]}".upper()
    if not initials.strip():
        initials = user.username[:2].upper()
    
    html = f'''
    <div class="user-avatar d-inline-flex align-items-center justify-content-center 
               rounded-circle bg-primary text-white" 
         style="width: {size}px; height: {size}px; font-size: {size//2.5}px;">
        {initials}
    </div>
    '''
    return mark_safe(html)

@register.simple_tag
def course_badge(course):
    """Generate course status badge"""
    if course.price == 0:
        return mark_safe('<span class="badge bg-success">Free</span>')
    else:
        return mark_safe(f'<span class="badge bg-primary">${course.price}</span>')

@register.filter
def truncate_words(value, arg):
    """Truncate text to specified number of words"""
    words = value.split()
    if len(words) > arg:
        return ' '.join(words[:arg]) + '...'
    return value