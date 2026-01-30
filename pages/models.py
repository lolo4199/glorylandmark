from django.db import models
from cloudinary.models import CloudinaryField

class Inquiry(models.Model):
    SERVICE_CHOICES = [
        ('REAL_ESTATE', 'Real Estate Inquiry'),
        ('CONSTRUCTION', 'Construction Project'),
        ('CONSULTANCY', 'Consultancy Services'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_display()}"
    
    
    


# For Construction Projects (Option A)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField(upload_to='projects/')
    completion_date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# For Consultancy FAQs (Option B)
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question    