from django.db import models


class Medication(models.Model):
    """Model representing a medication."""
    uuid = models.UUIDField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    released = models.DateField()

    def __str__(self) -> str:
        return self.name


class Disease(models.Model):
    """Model representing a disease."""
    name = models.CharField(max_length=200)
    medications = models.ManyToManyField(Medication, related_name='diseases')

    def __str__(self) -> str:
        return self.name
