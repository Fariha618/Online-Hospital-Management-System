from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    date_time = models.DateTimeField()  
    notes = models.TextField()
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    notes = models.TextField()
    prescription = models.TextField()
    details = models.TextField()

    def __str__(self):
        return f"Record for {self.patient.name} on {self.record_date}"
   
