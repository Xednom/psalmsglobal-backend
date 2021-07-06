from django.db import models

from apps.core.models import TimeStamped
from apps.post_paid.models import CustomerInteractionPostPaid


__all__ = ("InteractionRecord",)


class InteractionRecord(TimeStamped):
    date_called = models.DateField(auto_now_add=True)
    ticket_number = models.CharField(max_length=250, blank=True)
    customer_interaction_post_paid = models.ForeignKey(
        CustomerInteractionPostPaid,
        related_name="customer_interaction_post_paid_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    client = models.ForeignKey(
        "authentication.Client",
        related_name="post_paid_client_interaction_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    agent = models.ForeignKey(
        "authentication.Staff",
        related_name="post_paid_agent_interaction_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    total_minutes = models.IntegerField()
    summary = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]
    
    def __str__(self):
        return self.ticket_number
