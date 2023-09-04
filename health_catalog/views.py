from django.views.generic import ListView, DetailView
from django_filters.views import FilterView

from .filters import MedicationFilter, DiseaseFilter
from .models import Medication, Disease


class MedicationListView(FilterView, ListView):
    """
    View for listing all medications with filtering capabilities with pagination.
    """
    model = Medication
    template_name = 'medication_list.html'
    paginate_by = 10
    filterset_class = MedicationFilter
    context_object_name = 'medications'

    def get_context_data(self, **kwargs):
        """
        Override get_context_data to add query parameters to the context,
        excluding the 'page' parameter used for pagination, so the page urls don't stack up.
        """
        context = super().get_context_data(**kwargs)
        query_parameters = self.request.GET.copy()
        if 'page' in query_parameters:
            del query_parameters['page']
        context['query_parameters'] = query_parameters.urlencode()
        return context


class MedicationDetailView(DetailView):
    """
    View for displaying the details of a single medication.
    """
    model = Medication
    context_object_name = 'medication'
    template_name = 'medication_details.html'


class DiseaseListView(FilterView, ListView):
    """
    View for listing all diseases with filtering capabilities with pagination.
    """
    model = Disease
    template_name = 'disease_list.html'
    paginate_by = 10
    filterset_class = DiseaseFilter
    context_object_name = 'diseases'

    def get_context_data(self, **kwargs):
        """
        Override get_context_data to add query parameters to the context,
        excluding the 'page' parameter used for pagination, so the page urls don't stack up.
        """
        context = super().get_context_data(**kwargs)
        query_parameters = self.request.GET.copy()
        if 'page' in query_parameters:
            del query_parameters['page']
        context['query_parameters'] = query_parameters.urlencode()
        return context


class DiseaseDetailView(DetailView):
    """
    View for displaying the details of a single disease.
    """
    model = Disease
    context_object_name = 'disease'
    template_name = 'disease_details.html'
