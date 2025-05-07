from django.contrib import admin
from .models import Patient, Staff, Appointment, MedicalRecord

admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)

