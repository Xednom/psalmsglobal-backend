from django.db import models

from apps.post_paid.models import CustomerInteractionPostPaid, Acquisition


class TicketSummary(CustomerInteractionPostPaid):
    acquisition_tagging = models.ForeignKey(
        "post_paid.Acquisition",
        related_name="ticket_summary_acquisitions",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    prep_for_marketing = models.ForeignKey(
        "post_paid.Acquisition",
        related_name="ticket_summary_pre_for_marketings",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    disposition_tagging = models.ForeignKey(
        "post_paid.Acquisition",
        related_name="ticket_summary_dispotions",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    sales_team_assigned = models.ForeignKey(
        "authentication.Staff",
        related_name="ticket_summary_sales_team",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
