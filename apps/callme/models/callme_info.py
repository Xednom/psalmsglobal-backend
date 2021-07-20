from django.db import models

from apps.core.models import TimeStamped


__all__ = ("OfferStatus", "PropertyInfo", "PropertyFileInfo")


class OfferStatus(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class PropertyInfo(TimeStamped):
    company = models.ForeignKey(
        "callme.Company",
        related_name="company_customer_infos",
        on_delete=models.CASCADE,
    )
    apn = models.CharField(max_length=250, unique=True)
    reference = models.CharField(max_length=250, unique=True)
    property_size = models.CharField(max_length=250, blank=True)
    short_legal_description = models.TextField(blank=True)
    property_address = models.TextField(blank=True)
    property_city = models.TextField(blank=True)
    property_county = models.CharField(max_length=250, blank=True)
    property_state = models.CharField(max_length=250, blank=True)
    property_zip = models.CharField(max_length=250, blank=True)
    full_name = models.CharField(max_length=250, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    buyer_offer_amount = models.TextField(blank=True)
    approved_option_amount = models.TextField(blank=True)
    other_terms = models.TextField(blank=True)
    seller_offer_amount = models.TextField(blank=True)
    other_offer_terms = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    offer_status = models.ForeignKey(
        OfferStatus,
        related_name="customer_info_status",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    offer_status_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} - {self.apn}"


class PropertyFileInfo(TimeStamped):
    file = models.FileField(blank=True)

    def __str__(self):
        return self.file
