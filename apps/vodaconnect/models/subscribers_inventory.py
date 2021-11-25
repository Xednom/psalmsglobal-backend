from django.db import models

from apps.core.models import TimeStamped


__all__ = (
    "VoipInformation",
    "ActivationDetail",
    "PlanDetail",
    "SubscriberStatus",
    "ForwardingInformation",
    "TotalNumberOfExtension",
    "ZipTrunkLogin",
    "OtherLogin",
)


class PhoneLineStatus(models.TextChoices):
    inactive = "inactive", ("Inactive")
    active = "active", ("Active")
    cancelled = "cancelled", ("Cancelled")
    pending = "pending", ("Pending")


class ClientCompanyUserCategory(models.TextChoices):
    callme_com_ph = "callme_com_ph", ("CALLME.COM.PH")
    psalmsglobal = "psalmsglobal", ("PSALMSGLOBAL")
    landmaster = "landmaster", ("LANDMASTER")
    vodaconnect = "vodaconnect", ("VODACONNECT")


class RecurringBillChoices(models.TextChoices):
    yes = "yes", ("Yes")
    no = "no", ("No")
    pending = "pending", ("Pending")
    cancelled = "cancelled", ("Cancelled")


class TypeofRequest(models.TextChoices):
    new_number_request = "new_number_request", ("New number request")
    porting_request = "porting_request", ("Porting request")
    other_request = "other_request", ("Other request")


class Testimony(models.TextChoices):
    yes = "yes", ("Yes")
    no = "no", ("No")
    not_applicable = "not_applicable", ("Not Applicable")


class ProductionStatus(models.TextChoices):
    new_prospect = "new_prospect", ("New Prospect")
    new_request = "new_request", ("New Request")
    pending_request = "pending_request", ("Pending Request")
    call_email_follow_up = "call_email_follow_up", ("Call/Email follow up")
    ready_to_start = "ready_to_start", ("Ready to Start")
    sign_up_ready_for_setup = "sign_up_ready_for_setup", ("Sign up - Ready for Setup")
    active_live_in_production = "active_live_in_production", (
        "Active - Live in Production"
    )
    request_for_cancellation = "request_for_cancellation", ("Request for Cancellation")
    email_sent_for_cancellation = "email_sent_for_cancellation", (
        "Email sent for cancellation"
    )
    account_cancelled_by_vodaconnect = "account_cancelled_by_vodaconnect", (
        "Account cancelled by Vodaconnect"
    )
    recurring_charge_cancelled = "recurring_charge_cancelled", (
        "Recurring charge Cancelled"
    )
    account_cancelled = "account_cancelled", ("Account Cancelled")


class VoipInformation(TimeStamped):
    vodaconnect_number = models.CharField(max_length=250)
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_voip_information",
        on_delete=models.CASCADE,
    )
    client_code = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.client} vodaconnect number of {self.vodaconnect_number}"


class ActivationDetail(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_activation_detail",
        on_delete=models.CASCADE,
    )
    order_request_date = models.DateField()
    request_date_initiated = models.DateField()
    date_line_activated = models.DateField()
    date_line_terminated = models.DateField(blank=True, null=True)
    phone_line_status = models.CharField(
        max_length=30, choices=PhoneLineStatus.choices, blank=True
    )
    client_company_user_category = models.CharField(
        max_length=100, choices=ClientCompanyUserCategory.choices
    )


class PlanDetail(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_plan_detail",
        on_delete=models.CASCADE,
    )
    plan_type = models.ForeignKey(
        "vodaconnect.PlanType",
        related_name="plan_detail_plan_types",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    total_cost = models.DecimalField(
        max_digits=19, decimal_places=2, blank=True, null=True
    )
    recurring_bill = models.CharField(
        max_length=100, choices=RecurringBillChoices.choices
    )
    paypal_details_for_billing = models.TextField()
    due_date = models.DateField()


class SubscriberStatus(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_subscriber_statuses",
        on_delete=models.CASCADE,
    )
    status_in_production = models.CharField(
        max_length=250, choices=ProductionStatus.choices
    )
    type_of_request = models.CharField(max_length=250, choices=TypeofRequest.choices)
    testimony = models.CharField(max_length=20, choices=Testimony.choices)


class ForwardingInformation(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_forwarding_informations",
        on_delete=models.CASCADE,
    )
    forwarding_number = models.CharField(
        max_length=250, help_text="Customer's phone line"
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} {self.forwarding_number}"


class TotalNumberOfExtension(TimeStamped):
    forwarding_information = models.ForeignKey(
        ForwardingInformation,
        related_name="forwarding_information_total_number_of_extensions",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    extension_number = models.CharField(max_length=250)
    extension_logins = models.TextField(blank=True)
    notes = models.TextField(blank=True)


class ZipTrunkLogin(TimeStamped):
    forwarding_information = models.ForeignKey(
        ForwardingInformation,
        related_name="forwarding_information_zip_trunk_logins",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    zip_trunk_details = models.TextField()
    notes = models.TextField(blank=True)


class OtherLogin(TimeStamped):
    forwarding_information = models.ForeignKey(
        ForwardingInformation,
        related_name="forwarding_information_other_logins",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    description = models.TextField()
    notes = models.TextField(blank=True)
