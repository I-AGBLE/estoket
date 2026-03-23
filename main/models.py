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