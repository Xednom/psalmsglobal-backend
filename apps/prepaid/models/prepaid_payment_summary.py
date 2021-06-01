from django.db import models
from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("PaymentSummary",)


class PaymentSummary(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_payment_summaries",
        on_delete=models.CASCADE,
    )
    date_purchase = models.DateField()
    total_amount_paid = MoneyField(
        max_digits=19, decimal_places=2, default_currency="USD"
    )
    total_converted_minutes = models.DecimalField(max_digits=19, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]
    
    def __str__(self):
        return f"Payment summary of {self.client}"
