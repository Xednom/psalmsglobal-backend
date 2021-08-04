from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Crm",)


class Crm(TimeStamped):
    company = models.ForeignKey(
        "callme.Company", related_name="company_crms", on_delete=models.CASCADE
    )
    crm = models.BooleanField()
    type_of_crm = models.TextField(blank=True)
    crm_url = models.CharField(max_length=500, blank=True)
    crm_login = models.CharField(max_length=250, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-company"]
        verbose_name = "Type of Clients CRM"
        verbose_name_plural = "Type of Clients CRM"

    def __str__(self):
        return f"{self.company}"
