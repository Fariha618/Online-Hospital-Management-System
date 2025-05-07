# hospital/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('patients_portal/', views.patients_portal, name='patients_portal'),
    path('doctors_portal/', views.doctors_portal, name='doctors_portal'),
    path('login/', views.custom_login, name='custom_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),

    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/add/', views.patient_add, name='patient_add'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/add/', views.staff_add, name='staff_add'),
    path('staff/<int:pk>/edit/', views.staff_edit, name='staff_edit'),
    path('staff/delete/<int:pk>/', views.staff_delete, name='staff_delete'),

    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/add/', views.appointment_add, name='appointment_add'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('appointments/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
    path('appointments/approve/<int:pk>/', views.appointment_approve, name='appointment_approve'),
    path('appointments/cancel/<int:pk>/', views.appointment_cancel, name='appointment_cancel'),

    path('medical_records/', views.medical_record_list, name='medical_record_list'),
    path('medical_records/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    path('medical_records/add/', views.medical_record_add, name='medical_record_add'),
    path('medical_records/<int:pk>/edit/', views.medical_record_edit, name='medical_record_edit'),
    path('medical_records/delete/<int:pk>/', views.medical_record_delete, name='medical_record_delete'),
]