from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Property",)


class Property(TimeStamped):
    client_code = models.CharField(max_length=250, blank=True)
    full_name = models.CharField(max_length=250, blank=True)
    company_name = models.CharField(max_length=250, blank=True)
    reference_number = models.CharField(max_length=250, blank=True)
    apn = models.CharField(max_length=250, blank=True)
    county = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    size = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    price = models.CharField(max_length=250, blank=True)
    due_diligence = models.TextField(blank=True)
    ad_content = models.TextField(blank=True)
    images = models.TextField(blank=True)
    website = models.TextField(blank=True)
    comment_offer_tab_customer = models.TextField(blank=True)
    comment_offer_tab_client = models.TextField(blank=True)
    comment_sales_agent_notes = models.TextField(blank=True)
    facebook = models.CharField(max_length=250, blank=True)
    fb_groups = models.CharField(max_length=250, blank=True)
    landmodo = models.CharField(max_length=250, blank=True)
    fsbo = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    land_listing = models.CharField(max_length=250, blank=True)
    land_flip = models.CharField(max_length=250, blank=True)
    land_hub = models.CharField(max_length=250, blank=True)
    land_century = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ["-created_at"]
