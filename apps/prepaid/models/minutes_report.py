from django.db import models

from apps.core.models import TimeStamped


__all__ = ("MinutesReport",)


class MinutesReport(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_minutes_reports",
        on_delete=models.DO_NOTHING,
    )
    month_year = models.CharField(max_length=250)
    monthly_usage = models.IntegerField()
