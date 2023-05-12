from django.db import models

from apps.core.models import Tagging


__all__ = ["Acquisition", "PrepForMarketing", "Disposition", "OverallTagging"]


class Acquisition(models.Model):
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return f"{self.description}"


class PrepForMarketing(Tagging):
    # Inherited from Tagging

    def __str__(self):
        return f"{self.description}"


class Disposition(Tagging):
    # Inherited from Tagging

    def __str__(self):
        return f"{self.description}"


class OverallTagging(Tagging):
    # Inherited from Tagging

    def __str__(self):
        return f"{self.description}"
