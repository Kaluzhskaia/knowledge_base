from django_filters import FilterSet, CharFilter
from .models import Medication, Disease


class MedicationFilter(FilterSet):
    """
    A FilterSet for the Medication model.
    Provides filtering by name through a case-insensitive contains search.
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Medication
        fields = ['name']


class DiseaseFilter(FilterSet):
    """
    A FilterSet for the Disease model.
    Provides filtering by name through a case-insensitive contains search.
    """
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Disease
        fields = ['name']
