from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Subscription",)


class Subscription(TimeStamped):
    company = models.ForeignKey("callme.Company", on_delete=models.CASCADE)
    signed_up_date = models.DateField(blank=True, null=True)
    signed_out_date = models.DateField(blank=True, null=True)
    billing_cycle = models.DateField(blank=True, null=True)
    date_call_started = models.DateField(blank=True, null=True)
    status = models.BooleanField()
    script_created = models.BooleanField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-company"]
    
    def __str__(self):
        return f"{self.company} - {self.status}"