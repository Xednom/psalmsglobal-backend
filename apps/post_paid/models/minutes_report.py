from django.db import models
from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


class MinutesReport(TimeStamped):
    client = models.ForeignKey("authentication.Client", on_delete=models.DO_NOTHING)
    month_year = models.CharField(max_length=250)
    plan_type = models.CharField(max_length=250)
    cost_of_plan = MoneyField(max_digits=19, decimal_places=2, default_currency="USD")
    monthly_usage = models.IntegerField()
    total_minutes_unused = models.IntegerField()

    def __str__(self):
        return f"{self.client} minutes unused {self.total_minutes_unused}"