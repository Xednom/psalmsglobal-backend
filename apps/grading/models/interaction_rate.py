from django.db import models

from apps.core.models import TimeStamped


__all__ = ("PostpaidInteractionRate", "PrepaidInteractionRate", "TicketSummaryRate")


class PostpaidInteractionRate(TimeStamped):
    post_paid = models.ForeignKey(
        "post_paid.CustomerInteractionPostPaid",
        related_name="post_paid_interaction_rates",
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_post_paid_interaction_rates",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class PrepaidInteractionRate(TimeStamped):
    prepaid = models.ForeignKey(
        "prepaid.CustomerInteractionPrepaid",
        related_name="prepaid_interaction_rates",
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_prepaid_interaction_rates",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class TicketSummaryRate(TimeStamped):
    ticket_summary = models.ForeignKey(
        "post_paid.TicketSummary",
        related_name="ticket_summary_rates",
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()
    comment = models.TextField(blank=True)
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_ticket_summary_rates",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )