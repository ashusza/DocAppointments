from django.db import models
from app_Doctors.models import Doctor
from app_Patients.models import Patient

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient.patient_name} with {self.doctor.doctor_name} on {self.appointment_date}"

    class Meta:
        db_table = "Appointments"
        ordering = ["-appointment_date"]




        ## chatgpt ko ho yo ?
        ##