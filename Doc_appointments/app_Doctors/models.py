from django.db import models


# Create your models here.
class Specialist(models.Model):
    doctor_specialists = models.CharField(max_length =100)
    doctor_code = models.CharField(max_length=20,null= True)


    def __str__(self):
        return self.doctor_specialists
    
    
    class Meta:
        db_table = "Doctor_Specialists"
        ordering = ["-doctor_specialists"]

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_surname = models.CharField(max_length=100)
    doctor_img = models.FileField(upload_to="", blank=True, null=True)
    specialists = models.ForeignKey(Specialist,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.doctor_name + self.doctor_name + "-" + self.specialists.doctor_specialists

    
    class Meta:
        db_table = "doctor_list"
        ordering = ["-doctor_name"]
