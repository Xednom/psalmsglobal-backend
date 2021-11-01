from django.db import models

from apps.core.models import TimeStamped


__all__ = ("PlanType", "ActivePlanDetail")


class PlanType(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class ActivePlanDetail(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_vodaconnect_active_plan_details",
        on_delete=models.CASCADE,
    )
    plan_type = models.ForeignKey(
        PlanType,
        related_name="active_plan_detail_plan_types",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    total_minutes_included = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    cost_of_plan = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    start_of_plan = models.DateField()
    end_of_plan = models.DateField()
    account_status = models.BooleanField(default=True)
    recurring_bill = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.client} active plan detail"
