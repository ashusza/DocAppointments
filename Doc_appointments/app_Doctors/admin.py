from django.contrib import admin
from .models import Specialist,Doctor
# Register your models here.
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ["doctor_specialists","doctor_code"]

class DoctorAdmin(admin.ModelAdmin):
    list_display=("doctor_name","doctor_surname","specialists")

admin.site.register(Specialist,SpecialistAdmin)
admin.site.register(Doctor,DoctorAdmin)

