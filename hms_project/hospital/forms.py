from django import forms
from django.contrib.auth.models import User
from .models import Patient, Staff, Appointment, MedicalRecord

class PatientForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, required=False)  # Password is optional for updates

    class Meta:
        model = Patient
        fields = ['username', 'password', 'name', 'date_of_birth', 'address', 'phone', 'email']

    def save(self, commit=True):
        patient = super(PatientForm, self).save(commit=False)
        if not self.instance.pk:  # Create new user only if this is a new patient
            user = User.objects.create_user(
                self.cleaned_data['username'],
                password=self.cleaned_data['password']
            )
            patient.user = user
        if commit:
            patient.save()
        return patient

class StaffForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = ['username', 'password', 'name', 'position', 'hire_date']

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        staff = super(StaffForm, self).save(commit=False)
        staff.user = user
        if commit:
            staff.save()
        return staff

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'staff_member', 'date_time', 'notes', 'status']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'record_date', 'notes', 'prescription', 'details']