from django.db import models
from decimal import Decimal

from apps.core.models import TimeStamped


__all__ = ("PlanType", "CostPlan", "PostPaid")


class PlanType(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ["-name"]
        verbose_name = "Plan Type Category"
        verbose_name_plural = "Plan Type Category"

    def __str__(self):
        return self.name


class CostPlan(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ["-name"]
        verbose_name = "Cost of Plan"
        verbose_name_plural = "Cost of Plans"

    def __str__(self):
        return self.name


class PostPaid(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_post_paids",
        on_delete=models.DO_NOTHING,
    )
    plan_type = models.ForeignKey(
        PlanType, related_name="post_paid_plan_types", on_delete=models.DO_NOTHING
    )
    total_minutes = models.CharField(max_length=250)
    cost_of_plan = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True
    )
    start_of_plan = models.DateField(blank=True, null=True)
    end_of_plan = models.DateField(blank=True, null=True)
    account_status = models.BooleanField()
    recurring_bill = models.BooleanField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]
        verbose_name = "Active Plan Detail"
        verbose_name_plural = "Active Plan Details"

    def __str__(self):
        return f"{self.client} - {self.plan_type}"
