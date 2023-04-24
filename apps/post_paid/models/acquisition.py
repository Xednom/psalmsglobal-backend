from django.db import models


__all__ = ["Acquisition"]


class Acquisition(models.Model):
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)
