from import_export import resources

from apps.post_paid import models


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
            "billing_status",
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
            "customer_interaction_post_paid__ticket_number",
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


class CostPlanResource(resources.ModelResource):
    class Meta:
        model = models.CostPlan
        fields = ("name",)


class InterestedToBuyResource(resources.ModelResource):
    class Meta:
        model = models.InterestedToBuy
        fields = ("name",)


class InterestedToSellResource(resources.ModelResource):
    class Meta:
        model = models.InterestedToSell
        fields = ("name",)


class InternalAuditorResource(resources.ModelResource):
    class Meta:
        model = models.InternalAuditor
        fields = ("name",)


class JobOrderPostPaidResource(resources.ModelResource):
    class Meta:
        model = models.JobOrderPostPaid
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


class MonthlyChargeResource(resources.ModelResource):
    class Meta:
        model = models.MonthlyCharge
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "month_year",
            "plan_type",
            "total_minutes",
            "cost_of_plan",
            "payment_status",
            "payment_reference",
            "date_paid",
            "notes",
        )


class PlanTypeResource(resources.ModelResource):
    class Meta:
        model = models.PlanType
        fields = ("name",)


class CustomerInteractionPostPaidResource(resources.ModelResource):
    class Meta:
        model = models.CustomerInteractionPostPaid
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


class GeneralCallResource(resources.ModelResource):
    class Meta:
        model = models.GeneralCall
        fields = ("name",)


class TicketSummaryResource(resources.ModelResource):
    class Meta:
        model = models.TicketSummary
        fields = (
            "created_at",
            "updated_at",
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
            "acquisition_tagging",
            "prep_for_marketing",
            "disposition_tagging",
            "sales_team_assigned"
        )