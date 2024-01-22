from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=None # default display 
    
admin.site.register(Appointment)



    
