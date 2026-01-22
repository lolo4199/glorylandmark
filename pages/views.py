from django.shortcuts import render
from products.models import Property
from .models import Project

def home(request):
    # Fetch the 3 most recent properties
    latest_properties = Property.objects.filter(is_published=True).order_by('-list_date')[:3]
    # Fetch only 3 properties that are marked 'is_featured'
    featured_properties = Property.objects.filter(is_featured=True, is_published=True)[:3]
    # Fetch the 3 most recent construction projects
    recent_projects = Project.objects.order_by('-completion_date')[:3]
    
    context = {
        'latest_properties': latest_properties,
        'recent_projects': recent_projects,
        'featured_properties': featured_properties,
    }
    return render(request, 'pages/home.html', context)




from django.shortcuts import render, redirect
from .forms import InquiryForm
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! Our team will contact you soon.')
            return redirect('contact')
    else:
        # 1. Initialize empty data dictionary
        initial_data = {}
        
        # 2. Check for Consultancy Category
        category = request.GET.get('category', '')
        if category == 'CONSULTANCY':
            initial_data['service'] = 'CONSULTANCY'
            initial_data['message'] = 'I would like to book a professional consultation with GloryLandmark.'
        
        # 3. Check for Property Title (if coming from a Detail Page)
        property_title = request.GET.get('property', '')
        if property_title:
            initial_data['service'] = 'REAL_ESTATE' # Matches the dropdown choice
            initial_data['message'] = f"I am interested in the property: {property_title}. Please provide more details."
        
        # 4. Create the form once with all the gathered initial data
        form = InquiryForm(initial=initial_data)
        
    return render(request, 'pages/contact.html', {'form': form})





from .models import Project, FAQ

def construction(request):
    projects = Project.objects.all().order_by('-completion_date')
    return render(request, 'pages/construction.html', {'projects': projects})

def consultancy(request):
    faqs = FAQ.objects.all()
    return render(request, 'pages/consultancy.html', {'faqs': faqs})