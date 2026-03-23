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