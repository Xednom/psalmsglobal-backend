from django.db import models
from django.db.models.fields import DecimalField
from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("MonthlyCharge",)


class MonthlyCharge(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="post_paid_client_monthly_charges",
        on_delete=models.DO_NOTHING,
    )
    month_year = models.CharField(max_length=250)
    plan_type = models.CharField(max_length=250)
    total_minutes = models.DecimalField(max_digits=19, decimal_places=2)
    cost_of_plan = MoneyField(max_digits=19, decimal_places=2, default_currency="USD")
    payment_status = models.BooleanField(default=False)
    payment_reference = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]
        verbose_name = "Plan Summary and Payment"

    def __str__(self):
        return f"{self.client} {self.plan_type} {self.payment_status}"
