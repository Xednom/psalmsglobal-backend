from django.db import models

from apps.post_paid.models import (
    CrmChoices,
    LeadTransferredCrm,
)

__all__ = ["TicketSummary"]


class TicketSummary(models.Model):
    ticket_number = models.CharField(max_length=250, blank=True)
    company = models.ForeignKey(
        "callme.Company",
        related_name="ticket_summary_company",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    agent = models.ForeignKey(
        "authentication.Staff",
        related_name="ticket_summary_agents",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    apn = models.CharField(max_length=250, blank=True)
    reference_number = models.CharField(max_length=250, blank=True)
    county = models.CharField(max_length=250, blank=True)
    state = models.CharField(max_length=250, blank=True)
    address = models.TextField(blank=True)
    caller_full_name = models.CharField(max_length=250, blank=True)
    caller_phone = models.CharField(max_length=250, blank=True)
    email = models.CharField(max_length=250, blank=True)
    reason_of_the_call = models.TextField(blank=True)
    interested_to_sell = models.ForeignKey(
        "post_paid.InterestedToSell",
        related_name="ticket_summary_interested_to_sell",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    interested_to_buy = models.ForeignKey(
        "post_paid.InterestedToBuy",
        related_name="ticket_summary_interested_to_buy",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    general_call = models.ForeignKey(
        "post_paid.GeneralCall",
        related_name="ticket_summary_general_call",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    crm = models.CharField(max_length=250, choices=CrmChoices.choices, blank=True)
    leads_transferred_crm = models.CharField(
        max_length=250, choices=LeadTransferredCrm.choices, blank=True
    )
    internal_auditor = models.ForeignKey(
        "post_paid.InternalAuditor",
        related_name="ticket_summary_internal_auditors",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Ticket Summary"
        verbose_name_plural = "Ticket Summaries"
