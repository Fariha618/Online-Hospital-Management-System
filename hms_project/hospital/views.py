from django.shortcuts import render
from .models import Patient, Staff, Appointment, MedicalRecord
from .forms import PatientForm, StaffForm, AppointmentForm, MedicalRecordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

## Login users ###

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'staff'):
                    return redirect('doctors_portal')
                elif hasattr(user, 'patient'):
                    return redirect('patients_portal')
                else:
                    return redirect('dashboard')
        else:
            return render(request, 'admin_login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

##### Admin Login PAGE #####

@login_required
def dashboard(request):
    patients = Patient.objects.all()
    staff = Staff.objects.all()
    appointments = Appointment.objects.all()
    medical_records = MedicalRecord.objects.all()
    return render(request, 'hospital/dashboard.html', {
        'patients': patients,
        'staff': staff,
        'appointments': appointments,
        'medical_records': medical_records
    })

##### HOME PAGE #####
@login_required
def home(request):
    return render(request, 'hospital/home.html')

##### PATIENT #####
# Patient Portal

@login_required
def patients_portal(request):
    # Your logic here, e.g., fetching patient-specific data
    return render(request, 'hospital/patients_portal.html')

# List Patients
@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

# Detail of a Patient
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    appointments = Appointment.objects.filter(patient=patient)
    medical_records = MedicalRecord.objects.filter(patient=patient)

    return render(request, 'hospital/patient_detail.html', {
        'patient': patient,
        'appointments': appointments,
        'medical_records': medical_records
    })

# Add A Patient
from django.shortcuts import redirect

@login_required
def patient_add(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'hospital/patient_form.html', {'form': form})

# Edit Patient
from django.shortcuts import get_object_or_404

@login_required
def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            edited_patient = form.save(commit=False)
            user = edited_patient.user
            user.username = form.cleaned_data['username']
            if 'password' in form.cleaned_data and form.cleaned_data['password']:
                user.set_password(form.cleaned_data['password'])
            user.save()
            edited_patient.save()
            return redirect('patient_list')
    else:
        initial_data = {
            'username': patient.user.username,
            # Add other fields if necessary
        }
        form = PatientForm(instance=patient, initial=initial_data)

    return render(request, 'hospital/patient_form.html', {'form': form})

# Delete Patient
@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')
    return render(request, 'hospital/patient_confirm_delete.html', {'patient': patient})

##### STUFFS #####

#Doctor Portal
@login_required
def doctors_portal(request):
    # Your logic here, e.g., fetching patient-specific data
    return render(request, 'hospital/doctors_portal.html')

@login_required
def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'hospital/staff_list.html', {'staff_members': staff_members})

@login_required
def staff_detail(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    appointments = Appointment.objects.filter(staff_member=staff_member)  # Fetch related appointments
    return render(request, 'hospital/staff_detail.html', {
        'staff_member': staff_member,
        'appointments': appointments
    })

@login_required
def staff_add(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'hospital/staff_form.html', {'form': form})

@login_required
def staff_edit(request, pk):
    staff = Staff.objects.get(pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'hospital/staff_form.html', {'form': form})

def staff_delete(request, pk):
    staff_member = get_object_or_404(Staff, pk=pk)
    if request.method == "POST":
        staff_member.delete()
        return redirect('staff_list')
    return render(request, 'hospital/staff_confirm_delete.html', {'staff_member': staff_member})

##### APPOINTMENTS #####

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'hospital/appointment_detail.html', {'appointment': appointment})

@login_required
def appointment_add(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/appointment_form.html', {'form': form})

@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'hospital/appointment_form.html', {'form': form})

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'hospital/appointment_confirm_delete.html', {'appointment': appointment})

@login_required
def change_appointment_status(request, pk, status):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = status
    appointment.save()
    return redirect('appointment_list')

@login_required
def appointment_approve(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'approved'  # Assuming 'approved' is a valid status
    appointment.save()
    return redirect('appointment_list')

@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.status = 'canceled'  # Assuming 'canceled' is a valid status
    appointment.save()
    return redirect('appointment_list')

##### MEDICAL RECORDS #####

@login_required
def medical_record_list(request):
    records = MedicalRecord.objects.all()
    return render(request, 'hospital/medical_record_list.html', {'records': records})

@login_required
def medical_record_detail(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'hospital/medical_record_detail.html', {'record': record})

@login_required
def medical_record_add(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'hospital/medical_record_form.html', {'form': form})

@login_required
def medical_record_edit(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm(instance=record)
    return render(request, 'hospital/medical_record_form.html', {'form': form, 'cancel_url': 'medical_record_list'})

@login_required
def medical_record_delete(request, pk):
    record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('medical_record_list')
    return render(request, 'hospital/medical_record_confirm_delete.html', {'record': record})
