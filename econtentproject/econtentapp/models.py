from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"
    
class BibleAndManResource(models.Model):
    RESOURCE_TYPES = [
        ('ebook', 'Ebook'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    image = models.ImageField(upload_to='bible_and_man/images/', blank=True, null=True)
    file = models.FileField(upload_to='bible_and_man/') # for PDFS OR Videos
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class ClimateChangeResource(models.Model):
    RESOURCE_TYPES = [
        ('ebook', 'E-Book'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='climate_change/images/', blank=True, null=True)  # New field for image
    description = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='climate_change/resources/')  # For PDFs or Videos
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class HealthWellnessResource(models.Model):
    RESOURCE_TYPES = [
        ('ebook', 'E-Book'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='health_wellness/images/', blank=True, null=True)  # New field for image
    description = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='health_wellness/')  # For PDFs or Videos
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TrendyFashionResource(models.Model):
    RESOURCE_TYPES = [
        ('ebook', 'E-Book'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to='trendy_fashion/')  # PDFs or Videos
    cover_image = models.ImageField(upload_to='trendy_fashion/images/', blank=True, null=True)  # Optional Cover Image
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class EBook(models.Model):
    RESOURCE_TYPES = [
        ('ebook', 'E-Book'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='ebooks/covers/', blank=True, null=True)  
    file = models.FileField(upload_to='ebooks/files/', help_text="Upload PDF or Video")
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES, default='ebook')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class OnlineCourse(models.Model):
    COURSE_TYPES = [
        ('ebook', 'E-Book'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='online_courses/covers/', blank=True, null=True)  
    file = models.FileField(upload_to='online_courses/files/', help_text="Upload PDF or Video")
    course_type = models.CharField(max_length=10, choices=COURSE_TYPES, default='video')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title