from django.contrib import admin
from .models import PasswordReset
from .models import BibleAndManResource
from .models import ClimateChangeResource
from .models import TrendyFashionResource
from .models import EBook
from .models import OnlineCourse

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
