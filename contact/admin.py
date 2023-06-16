from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'subject',
        'content', 'date_submitted'
    )
admin.site.register(Contact, ContactAdmin)

