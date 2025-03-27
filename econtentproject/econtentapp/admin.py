from django.contrib import admin
from .models import PasswordReset
from .models import BibleAndManResource
from .models import ClimateChangeResource
from .models import TrendyFashionResource
from .models import EBook
from .models import OnlineCourse
from .models import NewsletterSubscription
from django.core.mail import send_mail
from django.contrib import admin
from django.conf import settings

# Register your models here.
admin.site.register(PasswordReset)

@admin.register(BibleAndManResource)
class BibleAndManResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'uploaded_by', 'date_uploaded')
    list_filter = ('resource_type', 'date_uploaded')
    search_fields = ('title', 'description')

@admin.register(ClimateChangeResource)
class ClimateChangeResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'uploaded_by', 'date_uploaded')
    list_filter = ('resource_type', 'date_uploaded')
    search_fields = ('title', 'description')

@admin.register(TrendyFashionResource)
class TrendyFashionResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'uploaded_by', 'date_uploaded')
    list_filter = ('resource_type', 'date_uploaded')
    search_fields = ('title', 'description')

@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'date_uploaded')
    search_fields = ('title', 'description')
    list_filter = ('date_uploaded',)

@admin.register(OnlineCourse)
class OnlineCourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_type', 'uploaded_at')
    list_filter = ('course_type', 'uploaded_at')
    search_fields = ('title', 'description')

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)
    actions = ['send_bulk_email']  # Custom admin action

    def send_bulk_email(self, request, queryset):
        subject = "New Newsletter from Fidelity Afriteam"
        message = "Hello,\n\nThis is our latest newsletter. Stay updated with our latest news!"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = queryset.values_list('email', flat=True)

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        self.message_user(request, "Emails sent successfully!")

    send_bulk_email.short_description = "Send Newsletter to selected emails"