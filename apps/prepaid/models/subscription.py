from django.db import models
from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("PlanType", "SubscriptionInfo", "PrepaidSubscription")


class PlanType(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class SubscriptionInfo(TimeStamped):
    company = models.ForeignKey(
        "callme.Company",
        related_name="prepaid_company_subscription_infos",
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
    date_paid = models.DateField(blank=True, null=True)
    month_year = models.CharField(max_length=250)
    plan_type = models.ForeignKey(
        PlanType,
        related_name="prepaid_plan_types",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    monthly_fee = MoneyField(
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

    def __str__(self):
        return f"{self.client} monthly subscription fee({self.monthly_fee}"
