from django.contrib import admin
from .models import Patient_Status,Patient
# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ["patient_status","patient_code"]

class PatientAdmin(admin.ModelAdmin):
    list_display = ["patient_name","patient_surname","status","patient_address","patient_number","patient_description"]
    
admin.site.register(Patient_Status,StatusAdmin)
admin.site.register(Patient,PatientAdmin)
