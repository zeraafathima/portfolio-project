from django.contrib import admin
from .models import Service  # Import your model
from .models import ContactMessage

admin.site.register(Service)  # Register it in the admin panel
admin.site.register(ContactMessage)
