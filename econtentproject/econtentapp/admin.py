from django.contrib import admin
from .models import PasswordReset
from .models import BibleAndManResource
from .models import ClimateChangeResource

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