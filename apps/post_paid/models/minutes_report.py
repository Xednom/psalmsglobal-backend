from django.db import models
from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("MinutesReport",)


class MinutesReport(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="post_paid_client_minutes_reports",
        on_delete=models.DO_NOTHING,
    )
    month_year = models.CharField(max_length=250)
    plan_type = models.CharField(max_length=250)
    cost_of_plan = MoneyField(max_digits=19, decimal_places=2, default_currency="USD")
    plan_allocated_minutes = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True
    )
    ci_minutes_overview = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    general_request_total_minutes = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    monthly_usage = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    total_minutes_unused = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )

    class Meta:
        verbose_name = "Month to Month Usage Overview"
        verbose_name_plural = "Month to Month Usage Overview"

    def __str__(self):
        return f"{self.client} minutes unused {self.total_minutes_unused}"
