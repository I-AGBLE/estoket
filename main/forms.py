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
        
from django import forms
from .models import FAQ

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['faq_question', 'faq_answer']

        labels = {
            'faq_question': '',
            'faq_answer': '',
        }

        widgets = {
            'faq_question': forms.TextInput(attrs={
                'placeholder': 'Enter FAQ question',
                'class': 'form-control'
            }),
            'faq_answer': forms.Textarea(attrs={
                'placeholder': 'Enter FAQ answer',
                'class': 'form-control',
                'rows': 3
            }),
        }
        

from django import forms
from .models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package_type', 'package_price', 'package_desc']

        labels = {
            'package_type': '',
            'package_price': '',
            'package_desc': '',
        }

        widgets = {
            'package_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'package_price': forms.NumberInput(attrs={
                'placeholder': 'Enter package price',
                'class': 'form-control'
            }),
            'package_desc': forms.Textarea(attrs={
                'placeholder': 'Describe the package',
                'class': 'form-control',
                'rows': 3
            }),
        }