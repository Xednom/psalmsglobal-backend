from django.db import models

from apps.core.models import TimeStamped
from apps.post_paid.models import CustomerInteractionPostPaid


__all__ = ("InteractionRecord",)


class StatusChoices(models.TextChoices):
    submitted = "submitted", ("Submitted")
    approved = "approved", ("Approved")


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
        null=True,
    )
    agent = models.ForeignKey(
        "authentication.Staff",
        related_name="post_paid_agent_interaction_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    total_minutes = models.IntegerField()
    summary = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.approved,
        blank=True,
    )

    class Meta:
        ordering = ["-client"]

    def __str__(self):
        return self.ticket_number
    
    def get_customer_interaction(self):
        client = self.customer_interaction_post_paid.company.client
        return client
    
    def save(self, *args, **kwargs):
        self.client = self.get_customer_interaction()
        super(InteractionRecord, self).save(*args, **kwargs)
