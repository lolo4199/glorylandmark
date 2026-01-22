from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    # We define the choices here to use in the subject field
    SERVICE_CHOICES = [
        ('', '--- Select Category ---'),
        ('REAL_ESTATE', 'Real Estate Inquiry'),
        ('CONSTRUCTION', 'Construction Project'),
        ('CONSULTANCY', 'Engineering Consultancy'),
        ('OTHER', 'Other'),
    ]

    # We override the subject field to use a Select widget with choices
    service = forms.ChoiceField(
        choices=SERVICE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Inquiry
        # Make sure these field names match exactly what is in your Inquiry model
        fields = ['name', 'email', 'service', 'message']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'How can we help you?'}),
        }