from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_title', 'about_service', 'service_image']

        labels = {
            'service_title': '',
            'about_service': '',
            'service_image': '',
        }

        widgets = {
            'service_title': forms.TextInput(attrs={
                'placeholder': 'Enter service title',
                'class': 'form-control'
            }),
            'about_service': forms.Textarea(attrs={
                'placeholder': 'Describe your service',
                'class': 'form-control',
                'rows': 4
            }),
        }
        

from django import forms
from .models import Expertise

class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = Expertise
        fields = ['expertise_title', 'about_expertise']

        labels = {
            'expertise_title': '',
            'about_expertise': '',
        }

        widgets = {
            'expertise_title': forms.TextInput(attrs={
                'placeholder': 'Enter expertise title',
                'class': 'form-control'
            }),
            'about_expertise': forms.Textarea(attrs={
                'placeholder': 'Describe your expertise',
                'class': 'form-control',
                'rows': 4
            }),
        }