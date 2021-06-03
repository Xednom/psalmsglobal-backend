from django.db import models

from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("AccountBalance",)


class AccountBalance(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="prepaid_client_account_balance",
        on_delete=models.CASCADE,
    )
    account_total_aquired_minutes = models.CharField(max_length=250, blank=True)
    account_total_mins_used = models.DecimalField(max_digits=19, decimal_places=2)
    account_total_mins_unused = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        ordering = ["-client"]
