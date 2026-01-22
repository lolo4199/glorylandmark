from django.urls import path
from .views import home, contact, construction, consultancy

urlpatterns = [
    path('', home, name='home'),
    path('construction/', construction, name='construction'),
    path('consultancy/', consultancy, name='consultancy'),
    path('contact/', contact, name='contact'),
]
