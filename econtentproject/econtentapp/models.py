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
    cover_image = models.ImageField(upload_to='bible_and_man_covers/', null=True, blank=True)
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
    file = models.FileField(upload_to='ebooks/files/')
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
    file = models.FileField(upload_to='online_courses/files/')
    course_type = models.CharField(max_length=10, choices=COURSE_TYPES, default='video')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
class NewsletterTemplate(models.Model):
    subject = models.CharField(max_length=255, default="Welcome to E-Content Platform!")
    content = models.TextField(default="""Dear Subscriber,

Thank you for joining our newsletter! You are now part of a growing community that enjoys exclusive access to valuable e-content, industry insights, and special updates.

✨ What You’ll Get:
✅ Latest updates on digital content and e-books  
✅ Exclusive access to special offers and announcements  
✅ Tips and resources to enhance your online experience  

Stay tuned for amazing content coming your way!  

Best regards,  
Fidelity AfriTeam  
""")

    def __str__(self):
        return self.subject