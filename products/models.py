from django.db import models
from cloudinary.models import CloudinaryField
class Property(models.Model):
    # Choices for the type of service
    CATEGORY_CHOICES = [
        ('SALE', 'For Sale'),
        ('RENT', 'For Rent'),
    ]

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='SALE')
    image = CloudinaryField('image') # Requires 'Pillow' library
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    list_date = models.DateTimeField(auto_now_add=True)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    sqft = models.IntegerField(default=0)

    def __str__(self):
        return self.title    
    

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image')  # Requires 'Pillow' library

    def __str__(self):
        return f"Image for {self.property.title}"    