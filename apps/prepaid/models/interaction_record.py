from django.db import models

from apps.core.models import TimeStamped
from apps.prepaid.models import CustomerInteractionPrepaid


__all__ = ("InteractionRecord",)


class FeedBackStatus(models.TextChoices):
    dispute = "dispute", ("Dispute")
    na = "n/a", ("N/A")
    clarification = "clarification", ("Clarification")
    case_closed = "case_closed", ("Case Closed")
    dispute_on_progress = "dispute_on_progress", ("Dispute on progress")
    resolution_given = "resolution_given", ("Resolution given")
    other = "other", ("Other")


class TicketStatus(models.TextChoices):
    na = "na", ("N/A")
    case_closed = "case_closed", ("Case Closed")
    dispute_on_progress = "dispute_on_progress", ("Dispute on progress")
    resolution_given = "resolution_given", ("Resolution given")
    others = "others", ("Others")


class StatusChoices(models.TextChoices):
    submitted = "submitted", ("Submitted")
    approved = "approved", ("Approved")


class InteractionRecord(TimeStamped):
    date_called = models.DateField(auto_now_add=True)
    ticket_number = models.CharField(max_length=250, blank=True)
    customer_interaction_prepaid = models.ForeignKey(
        CustomerInteractionPrepaid,
        related_name="customer_interaction_prepaid_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    client = models.ForeignKey(
        "authentication.Client",
        related_name="prepaid_client_interaction_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    agent = models.ForeignKey(
        "authentication.Staff",
        related_name="prepaid_agent_interaction_records",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    total_minutes = models.DecimalField(
        max_digits=19, decimal_places=2, default=0.00, blank=True, null=True
    )
    summary = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.approved,
        blank=True,
    )
    client_feedback_status = models.CharField(
        max_length=100,
        choices=FeedBackStatus.choices,
        default=FeedBackStatus.na,
        blank=True,
    )
    dispute_details = models.TextField(blank=True)
    other_feedback = models.TextField(blank=True)
    client_notes = models.TextField(blank=True)
    internal_management_ticket_status = models.CharField(
        max_length=100,
        choices=TicketStatus.choices,
        default=TicketStatus.na,
        blank=True,
    )
    memo_solution_from_the_mgmt = models.TextField(blank=True)
    other_ticket_status = models.TextField(blank=True)

    class Meta:
        ordering = ["-client"]
        verbose_name = "Call Record Breakdown"
        verbose_name_plural = "Call Record Breakdown"

    def __str__(self):
        return self.ticket_number

    def get_customer_interaction(self):
        if self.customer_interaction_prepaid.company.client:
            client = self.customer_interaction_prepaid.company.client
            return client
        elif self.client:
            return self.client

    def save(self, *args, **kwargs):
        # self.client = self.get_customer_interaction()
        super(InteractionRecord, self).save(*args, **kwargs)
