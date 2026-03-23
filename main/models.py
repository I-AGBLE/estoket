from django.db import models

# Create your models here.
from django.db import models

class Service(models.Model):
    service_title = models.CharField(max_length=255)
    service_image = models.ImageField(upload_to='services/')
    about_service = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_title
    
    
    
class Expertise(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='expertise')
    expertise_title = models.CharField(max_length=255)
    about_expertise = models.TextField()

    def __str__(self):
        return self.expertise_title
    
    

class FAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    faq_question = models.CharField(max_length=255)
    faq_answer = models.TextField()

    def __str__(self):
        return self.faq_question
    
    
from django.db import models

class Package(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='packages')
    package_type = models.CharField(max_length=20, choices=PACKAGE_CHOICES)
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_desc = models.TextField()

    def __str__(self):
        return f"{self.package_type} - {self.package_price}"