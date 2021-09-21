from django.db import models

from apps.core.models import TimeStamped


__all__ = ("SubscriptionType", "Prepaid")


class SubscriptionType(TimeStamped):
    name = models.CharField(max_lenghth=250)

    def __str__(self):
        return f"{self.name}"


class Prepaid(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_prepaid_accounts",
        on_delete=models.CASCADE,
    )
    subscription_type = models.ForeignKey(
        SubscriptionType, related_name="prepaid_subscription_types"
    )
    monthly_fees = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    start_of_subscription = models.DateField()
    end_of_subscription = models.DateField()
    account_status = models.BooleanField(default=False, blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name = "Prepaid"

    def __str__(self):
        return f"{self.client} Prepaid info"
