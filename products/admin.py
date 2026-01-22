from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]