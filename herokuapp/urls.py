from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<list_id>', views.delete, name="delete"),
    path('patient_not_attended_to/<list_id>', views.patient_not_attended_to, name="patient_not_attended_to"),
    path('patient_attended_to/<list_id>', views.patient_attended_to, name="patient_attended_to"),
    path('edit/<list_id>', views.edit, name="edit"),
]