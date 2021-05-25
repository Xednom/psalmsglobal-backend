from django.db import models

from apps.core.models import TimeStamped


class Crm(TimeStamped):
    company = models.ForeignKey("callme.Company", on_delete=models.CASCADE)
    crm = models.BooleanField()
    type_of_crm = models.TextField()
    crm_url = models.CharField(max_length=500)
    crm_login = models.CharField(max_length=250)
    notes = models.TextField()

    class Meta:
        ordering = ["-company"]
    
    def __str__(self):
        return f"{self.company}"
