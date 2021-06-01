from django.db import models
from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("SubscriptionInfo", "PrepaidSubscription")


class SubscriptionInfo(TimeStamped):
    company = models.ForeignKey(
        "callme.Company",
        related_name="company_subscription_infos",
        on_delete=models.CASCADE,
    )
    signed_up_date = models.DateField(blank=True, null=True)
    signed_out_date = models.DateField(blank=True, null=True)
    date_of_subscription_starts = models.DateField(blank=True, null=True)
    status = models.BooleanField()
    script_created = models.BooleanField()
    notes = models.TextField(blank=True)


class PrepaidSubscription(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_prepaid_subscriptions",
        on_delete=models.DO_NOTHING,
    )
    month_year = models.CharField(max_length=250)
    monthly_subscription = models.CharField(max_length=250)
    amount = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )
    payment_status = models.BooleanField()
    payment_reference = models.TextField(blank=True)
    notes = models.TextField(blank=True)
