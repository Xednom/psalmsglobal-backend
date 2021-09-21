from django.db import models

from apps.core.models import TimeStamped


__all__ = ("MinutesReport",)


class MinutesReport(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="prepaid_client_minutes_reports",
        on_delete=models.DO_NOTHING,
    )
    month_year = models.CharField(max_length=250)
    customer_interaction_mins_overview = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    general_request_mins_overview = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    consumed_minutes = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
