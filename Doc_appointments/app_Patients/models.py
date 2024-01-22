from django.db import models

# Create your models here.
class Patient_Status(models.Model):
    patient_status = models.CharField(max_length=100)
    patient_code = models.CharField(max_length=100)
    

    def __str__(self):
        return self.patient_status
    
    class Meta:
        db_table = "Patient_Details"
        ordering = ["-patient_status"]
        
class Patient(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_surname = models.CharField(max_length=100)
    patient_address = models.CharField(max_length=100)
    status = models.ForeignKey(Patient_Status,on_delete=models.CASCADE)
    patient_number = models.IntegerField(null=True)
    patient_description = models.CharField(max_length=100)

    def __str__(self):
        return self.patient_name + self.patient_surname 
    
    class Meta:
        db_table = "Patient_list"
        ordering = ["-patient_name"]

    
    


    