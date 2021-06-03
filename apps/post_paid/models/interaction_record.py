from django.db import models

from apps.core.models import TimeStamped


__all__ = ("InteractionRecord",)


class InteractionRecord(TimeStamped):
    date_called = models.DateField(auto_now_add=True)
    client = models.ForeignKey(
        "authentication.Client",
        related_name="post_paid_client_interaction_records",
        on_delete=models.DO_NOTHING,
    )
    agent = models.ForeignKey(
        "authentication.Staff",
        related_name="post_paid_agent_interaction_records",
        on_delete=models.DO_NOTHING,
    )
    total_minutes = models.IntegerField()
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]
