from django import forms
from .models import BibleAndManResource

class BibleAndManResourceForm(forms.ModelForm):
    class Meta:
        model = BibleAndManResource
        fields = ['title', 'description', 'resource_type', 'image', 'file']