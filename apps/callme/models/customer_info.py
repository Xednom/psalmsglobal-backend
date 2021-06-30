from django.db import models

from apps.core.models import TimeStamped


__all__ = ("OfferStatus", "CustomerInfo")


class OfferStatus(TimeStamped):
    name = models.CharField(max_length=250)


class CustomerInfo(TimeStamped):
    company = models.ForeignKey(
        "callme.Company",
        related_name="company_customer_infos",
        on_delete=models.CASCADE,
    )
    apn = models.CharField(max_length=500)
    reference = models.CharField(max_length=500)
    property_size = models.CharField(max_length=250)
    short_legal_description = models.TextField()
    property_address = models.TextField()
    property_city = models.TextField()
    property_county = models.CharField(max_length=250)
    property_state = models.CharField(max_length=250)
    property_zip = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    offer_amount = models.TextField()
    approved_option_amount = models.TextField()
    other_terms = models.TextField()
    offer_amount = models.TextField()
    other_offer_terms = models.TextField()
    notes = models.TextField()
    offer_status = models.ForeignKey(
        OfferStatus, related_name="customer_info_status", on_delete=models.DO_NOTHING
    )
    offer_status_notes = models.TextField()
