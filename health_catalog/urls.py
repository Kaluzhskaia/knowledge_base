from django.urls import path
from .views import MedicationListView, DiseaseListView, DiseaseDetailView, MedicationDetailView

urlpatterns = [
    # URLs for listing all medications
    path('', MedicationListView.as_view(), name='medication_list'),
    path('medications/', MedicationListView.as_view(), name='medication_list'),

    # URL for displaying details of a specific medication identified by 'pk'
    path('medication_details/<int:pk>/', MedicationDetailView.as_view(), name='medication_details'),

    # URL for listing all diseases
    path('diseases/', DiseaseListView.as_view(), name='disease_list'),

    # URL for displaying details of a specific disease identified by 'pk'
    path('disease_details/<int:pk>/', DiseaseDetailView.as_view(), name='disease_details'),
]

