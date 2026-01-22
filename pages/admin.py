from django.contrib import admin
from .models import Project, FAQ, Inquiry

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'completion_date') # Columns in the list
    search_fields = ('title', 'location') # Adds a search bar
    list_filter = ('completion_date',) # Adds a sidebar filter

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'date_sent')
    readonly_fields = ('date_sent',) # Prevents admin from changing the date