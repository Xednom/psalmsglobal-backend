from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Company",)


class BusinessTypeChoices(models.TextChoices):
    individual = "individual", ("Individual")
    partnership = "partnership", ("Partnership")
    corporation = "corporation", ("Corporation")
    llcs = "llcs", ("LLCs")
    others = "others", ("Others")


class Company(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_companies",
        on_delete=models.DO_NOTHING,
    )
    company_owner_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    business_type = models.CharField(
        max_length=250, choices=BusinessTypeChoices.choices
    )
    company_phone = models.CharField(max_length=250)
    company_email = models.CharField(max_length=250)
    company_complete_address = models.TextField()
    company_forwarding_email = models.CharField(max_length=250)
    paypal_email = models.CharField(max_length=250)
    notes = models.TextField()

    class Meta:
        verbose_name = "List of Company"
        verbose_name_plural = "List of Companies"
        ordering = ["-client"]

    def __str__(self):
        return f"{self.company_owner_name} {self.company_name} - {self.client}"
