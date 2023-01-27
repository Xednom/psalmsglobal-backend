from import_export import resources

from apps.prepaid import models


class AccountBalanceResource(resources.ModelResource):
    class Meta:
        model = models.AccountBalance
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "account_total_aquired_minutes",
            "account_total_spending",
            "account_total_mins_used",
            "account_total_mins_unused",
            "total_spending",
        )


class AccountChargeResource(resources.ModelResource):
    class Meta:
        model = models.AccountCharge
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "agent__user__first_name",
            "agent__user__last_name",
            "ticket_number",
            "date_called",
            "total_minutes",
            "summary",
        )


class InteractionRecordResource(resources.ModelResource):
    class Meta:
        model = models.InteractionRecord
        fields = (
            "date_called",
            "ticket_number",
            "customer_interaction_prepaid__ticket_number",
            "client__user__first_name",
            "client__user__last_name",
            "agent__user__first_name",
            "agent__user__last_name",
            "total_minutes",
            "summary",
            "status",
            "client_feedback_status",
            "dispute_details",
            "other_feedback",
            "client_notes",
            "internal_management_ticket_status",
            "memo_solution_from_the_mgmt",
            "other_ticket_status",
        )


class JobOrderPrepaidResource(resources.ModelResource):
    class Meta:
        model = models.JobOrderPrepaid
        fields = (
            "caller_interaction_record__ticket_number",
            "client__user__first_name",
            "client__user__last_name",
            "client_file",
            "client_email",
            "va_assigned",
            "staff_email",
            "ticket_number",
            "request_date",
            "due_date",
            "job_title",
            "job_description",
            "client_notes",
            "va_notes",
            "management_notes",
            "status",
            "date_completed",
            "total_time_consumed",
            "url_of_the_completed_jo",
        )


class MinutesReportResource(resources.ModelResource):
    class Meta:
        model = models.MinutesReport
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "month_year",
            "customer_interaction_mins_overview",
            "general_request_mins_overview",
            "consumed_minutes",
        )


class PaymentSummaryResource(resources.ModelResource):
    class Meta:
        model = models.PaymentSummary
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "date_purchase",
            "total_amount_paid",
            "total_converted_minutes",
            "payment_reference",
            "payment_channel",
            "notes",
        )


class PlanTypeResource(resources.ModelResource):
    class Meta:
        model = models.PlanType
        fields = ("name",)


class CustomerInteractionPrepaidResource(resources.ModelResource):
    class Meta:
        model = models.CustomerInteractionPrepaid
        fields = (
            "ticket_number",
            "company",
            "agent",
            "apn",
            "reference_number",
            "county",
            "state",
            "address",
            "caller_full_name",
            "caller_phone",
            "email",
            "reason_of_the_call",
            "interested_to_sell",
            "interested_to_buy",
            "general_call",
            "crm",
            "leads_transferred_crm",
            "internal_auditor",
        )


class PrepaidSubscriptionResource(resources.ModelResource):
    class Meta:
        model = models.PrepaidSubscription
        fields = (
            "client",
            "date_paid",
            "month_year",
            "plan_type",
            "monthly_fee",
            "payment_status",
            "payment_reference",
            "notes",
        )


class PrepaidResource(resources.ModelResource):
    class Meta:
        model = models.Prepaid
        fields = (
            "client",
            "date_paid",
            "month_year",
            "plan_type",
            "monthly_fee",
            "payment_status",
            "payment_reference",
            "notes",
        )


class SubscriptionTypeResource(resources.ModelResource):
    class Meta:
        model = models.SubscriptionType
        fields = ("name",)
