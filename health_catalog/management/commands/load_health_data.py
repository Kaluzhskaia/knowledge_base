from django.core.management.base import BaseCommand
from health_catalog.models import Medication, Disease
import json
from datetime import datetime
from typing import Any, Dict


class Command(BaseCommand):
    """
    A Django management command to load medication and disease data from a JSON file into the database.

    Attributes:
        help (str): A help string displayed when running the command with '--help'.
    """

    help = 'Load medication and disease data from a JSON file into the database.'

    def add_arguments(self, parser: Any) -> None:
        """
        Define the command-line arguments that the command expects.

        Args:
            parser: The parser to which the command-line arguments should be added.
        """
        parser.add_argument('json_file', type=str, help='The JSON file path')

    def handle(self, *args: Any, **kwargs: Dict[str, Any]) -> None:
        """
        Handle the logic for loading medication and disease data into the database.

        Args:
            args: Variable-length argument list.
            kwargs: Arbitrary keyword arguments containing command-line options.
        """
        json_file = kwargs['json_file']

        with open(json_file, 'r') as f:
            data = json.load(f)

        for medication_data in data['drugs']:
            medication = Medication(
                uuid=medication_data['id'],
                name=medication_data['name'],
                description=medication_data['description'],
                released=datetime.strptime(medication_data['released'], '%Y-%m-%d').date()
            )
            medication.save()

            for disease_name in medication_data['diseases']:
                disease, created = Disease.objects.get_or_create(name=disease_name)
                disease.medications.add(medication)

        self.stdout.write(self.style.SUCCESS('Successfully loaded data into the database'))
