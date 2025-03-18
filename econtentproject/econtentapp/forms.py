from django import forms
from .models import BibleAndManResource
from .models import ClimateChangeResource

class BibleAndManResourceForm(forms.ModelForm):
    class Meta:
        model = BibleAndManResource
        fields = ['title', 'description', 'resource_type', 'image', 'file']

class ClimateChangeResourceForm(forms.ModelForm):
    class Meta:
        model = ClimateChangeResource
        fields = ['title', 'cover_image', 'description', 'resource_type', 'file']