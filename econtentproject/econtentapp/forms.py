from django import forms
from .models import BibleAndManResource
from .models import ClimateChangeResource
from .models import HealthWellnessResource
from .models import TrendyFashionResource
from .models import EBook
from .models import OnlineCourse
from .models import NewsletterSubscription


class BibleAndManResourceForm(forms.ModelForm):
    class Meta:
        model = BibleAndManResource
        fields = ['title', 'description', 'resource_type', 'cover_image', 'file']

class ClimateChangeResourceForm(forms.ModelForm):
    class Meta:
        model = ClimateChangeResource
        fields = ['title', 'description', 'resource_type', 'cover_image', 'file']

class HealthWellnessResourceForm(forms.ModelForm):
    class Meta:
        model = HealthWellnessResource
        fields = ['title', 'description', 'resource_type', 'cover_image', 'file']

class TrendyFashionResourceForm(forms.ModelForm):
    class Meta:
        model = TrendyFashionResource
        fields = ['title', 'description', 'resource_type', 'file', 'cover_image']

class EBookForm(forms.ModelForm):
    class Meta:
        model = EBook
        fields = ['title', 'description', 'cover_image', 'file']

class OnlineCourseForm(forms.ModelForm):
    class Meta:
        model = OnlineCourse
        fields = ['title', 'description', 'cover_image', 'file', 'course_type']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']