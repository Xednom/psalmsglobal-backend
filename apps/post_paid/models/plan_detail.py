from django.db import models

from apps.core.models import TimeStamped


class PlanType(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class CostPlan(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class PostPaid(TimeStamped):
    client = models.ForeignKey("authentication.Client", on_delete=models.DO_NOTHING)
    plan_type = models.ForeignKey(PlanType, on_delete=models.DO_NOTHING)
    total_minutes = models.CharField(max_length=250)
    cost_of_plan = models.ForeignKey(CostPlan, on_delete=models.DO_NOTHING)
    start_of_plan = models.CharField(max_length=250)
    end_of_plan = models.CharField(max_length=250)
    account_status = models.BooleanField()
    recurring_bill = models.BooleanField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]

    def __str__(self):
        return f"{self.client} - {self.plan_type}"
