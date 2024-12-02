from django.contrib import admin

# Register your models here.
from .models import Blog  # Change 'Recipe' to your new model name, e.g., 'Event'

admin.site.register(Blog)  # Ensure this matches the model you want to register
