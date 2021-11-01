from django.db import models

from apps.core.models import TimeStamped


__all__ = ("PlanSummaryAndPayment",)


class PlanSummaryAndPayment(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_plan_summary_and_payments",
        on_delete=models.CASCADE,
    )
    month_year = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=250)
    total_minutes = models.DecimalField(max_digits=19, decimal_places=2)
    cost_of_plan = models.DecimalField(max_digits=19, decimal_places=2)
    payment_reference = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    date_of_paid = models.DateField()
