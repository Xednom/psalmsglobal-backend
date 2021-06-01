from django.db import models

from apps.core.models import TimeStamped


__all__ = ("VodaconnectPlan", "VodaconnectLineType", "PhoneSystem")


class VodaconnectPlan(TimeStamped):
    range = models.CharField(max_length=100)

    def __str__(self):
        return self.range


class VodaconnectLineType(TimeStamped):
    line = models.CharField(max_length=250)

    def __str__(self):
        return self.line


class PhoneSystem(TimeStamped):
    company = models.ForeignKey(
        "callme.Company", related_name="company_phone_systems", on_delete=models.CASCADE
    )
    sub_number = models.BooleanField()
    caller_id_detail = models.TextField()
    vodaconnect_plan = models.ForeignKey(
        VodaconnectPlan,
        related_name="vodaconnect_plan_phone_systems",
        on_delete=models.DO_NOTHING,
    )
    original_line = models.CharField(max_length=250)
    call_forwarding_number = models.CharField(max_length=250)
    vodaconnect_line_type = models.ForeignKey(
        VodaconnectLineType,
        related_name="vodaconnect_line_type_phone_systems",
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ["-company"]

    def __str__(self):
        return f"{self.company} - {self.sub_number}"
