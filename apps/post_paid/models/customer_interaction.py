from django.db import models

from apps.core.models import TimeStamped


__all__ = (
    "LeadTransferredCrm",
    "InterestedToSell",
    "InterestedToBuy",
    "GeneralCall",
    "CustomerInteractionPostPaid",
    "CustomerInteractionPostPaidComment",
)


class CrmChoices(models.TextChoices):
    yes = "yes", ("yes")
    no = "no", ("No")
    needs_validation = "needs_validation", ("Needs validation")
    invalid_data = "invalid_data", ("Invalid data")
    needs_follow_up = "needs_follow_up", ("Needs follow-up")


class LeadTransferredCrm(models.TextChoices):
    needs_transferred = "needs_transferred", ("Needs transferred")
    transfer_complete = "transfer_complete", ("Transfer complete")
    na = "na", ("N/A")


class InterestedToSell(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class InterestedToBuy(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class GeneralCall(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class CustomerInteractionPostPaid(TimeStamped):
    ticket_number = models.CharField(max_length=250, blank=True)
    company = models.ForeignKey(
        "callme.Company",
        related_name="post_paid_company_customer_interaction",
        on_delete=models.DO_NOTHING,
    )
    apn = models.CharField(max_length=250)
    caller_full_name = models.CharField(max_length=250)
    caller_phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    reason_of_the_call = models.TextField(blank=True)
    interested_to_sell = models.ForeignKey(
        InterestedToSell,
        related_name="post_paid_interested_to_sell_interactions",
        on_delete=models.CASCADE,
    )
    interested_to_buy = models.ForeignKey(
        InterestedToBuy,
        related_name="post_paid_interested_to_buy_interactions",
        on_delete=models.CASCADE,
    )
    general_call = models.ForeignKey(
        GeneralCall,
        related_name="post_paid_customer_interaction_general_calls",
        on_delete=models.CASCADE,
    )
    crm = models.CharField(max_length=250, choices=CrmChoices.choices)
    leads_transferred_crm = models.CharField(
        max_length=250, choices=LeadTransferredCrm.choices
    )

    def create_ticket_number(self):
        ticket_code = ""
        last_in = CustomerInteractionPostPaid.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            ticket_number = "CI000" + str((int(seq) + 1))
            return ticket_number

        if self.id:
            if self.id >= 100:
                ticket_number = "CI" + str(self.id)
            elif self.id <= 9:
                ticket_number = "CI00" + str(self.id)
            elif self.id >= 10:
                ticket_number = "CI0" + str(self.id)
            return ticket_number

        in_id = last_in.id
        in_int = int(in_id)
        if in_int >= 100:
            ticket_code = "CI" + str(int(in_int) + 1)
        elif in_int < 10:
            ticket_code = "CI00" + str(int(in_int) + 1)
        elif in_int >= 10:
            ticket_code = "CI0" + str(int(in_int) + 1)
        
        return ticket_code

    def save(self, *args, **kwargs):
        self.ticket_number = self.create_ticket_number()
        super(CustomerInteractionPostPaid, self).save(*args, **kwargs)


class CustomerInteractionPostPaidComment(TimeStamped):
    customer_interaction_post_paid = models.ForeignKey(
        CustomerInteractionPostPaid,
        related_name="customer_interaction_post_paid_comments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        "authentication.User", on_delete=models.SET_NULL, blank=True, null=True
    )
    comment = models.TextField()

    class Meta:
        ordering = ["-created_at"]
