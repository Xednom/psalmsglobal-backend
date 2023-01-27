from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.prepaid.models import (
    AccountBalance,
    AccountCharge,
    Prepaid,
    CustomerInteractionPrepaid,
    InteractionRecord,
    MinutesReport,
    JobOrderPrepaid,
    PrepaidSubscription,
    SubscriptionType,
    PaymentSummary,
)

from apps.prepaid import resources


class AccountBalanceAdmin(ImportExportModelAdmin):
    model = AccountBalance
    resources = resources.AccountBalanceResource
    list_display = (
        "client",
        "account_total_aquired_minutes",
        "account_total_spending",
        "account_total_mins_used",
        "account_total_mins_unused",
    )
    list_filter = ("client",)
    search_fields = ("client__user__first_name", "client__user__last_name")
    readonly_fields = ("created_at", "updated_at")


class AccountChargeAdmin(ImportExportModelAdmin):
    model = AccountCharge
    resources = resources.AccountChargeResource
    list_display = ("client", "agent", "ticket_number", "date_called", "total_minutes")
    list_filter = ("client", "agent")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "agent__user__first_name",
        "agent__user__last_name",
    )
    readonly_fields = ("created_at", "updated_at")


class CustomerInteractionPrepaidAdmin(ImportExportModelAdmin):
    model = CustomerInteractionPrepaid
    resources = resources.CustomerInteractionPrepaidResource
    list_display = (
        "id",
        "ticket_number",
        "created_at",
        "company",
        "apn",
        "reference_number",
        "state",
        "crm",
        "leads_transferred_crm",
        "internal_auditor",
        "caller_full_name",
        "caller_phone",
        "email",
        "interested_to_sell",
        "interested_to_buy",
        "general_call",
        "agent",
    )
    list_filter = (
        "company__company_name",
        "agent",
        "county",
        "state",
        "crm",
        "leads_transferred_crm",
        "internal_auditor",
        "interested_to_sell",
        "interested_to_buy",
        "general_call",
    )
    search_fields = (
        "ticket_number",
        "company__client__user__first_name",
        "company__client__user__last_name",
        "county",
        "state",
        "crm",
        "leads_transferred_crm",
        "internal_auditor__name",
        "interested_to_sell__name",
        "interested_to_buy__name",
        "general_call__name",
        "agent__user__first_name",
        "agent__user__last_name",
    )
    readonly_fields = ("created_at", "updated_at")


class InteractionRecordAdmin(ImportExportModelAdmin):
    model = InteractionRecord
    resources = resources.InteractionRecordResource
    list_display = (
        "client",
        "agent",
        "date_called",
        "total_minutes",
        "client_feedback_status",
        "internal_management_ticket_status",
    )
    list_filter = ("client", "agent", "date_called")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "agent__user__first_name",
        "agent__user__last_name",
        "date_called",
    )
    readonly_fields = ("created_at", "updated_at")


class MinutesReportAdmin(ImportExportModelAdmin):
    model = MinutesReport
    resources = resources.MinutesReportResource
    list_display = (
        "created_at",
        "id",
        "client",
        "month_year",
        "customer_interaction_mins_overview",
        "general_request_mins_overview",
        "consumed_minutes",
    )
    list_filter = ("client", "month_year")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "month_year",
    )
    readonly_fields = ("created_at", "updated_at")


class PrepaidAdmin(ImportExportModelAdmin):
    model = Prepaid
    resources = resources.PrepaidResource
    list_display = (
        "client",
        "subscription_type",
        "monthly_fees",
        "start_of_subscription",
        "end_of_subscription",
        "account_status",
    )
    list_filter = ("client", "account_status")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name" "subscription_type__name",
    )
    readonly_fields = ("created_at", "updated_at")


class JobOrderAdmin(ImportExportModelAdmin):
    model = JobOrderPrepaid
    resources = resources.JobOrderPrepaidResource
    list_display = (
        "client",
        "client_file",
        "client_email",
        "request_date",
        "due_date",
        "job_title",
        "job_title",
        "status",
        "date_completed",
        "total_time_consumed",
        "url_of_the_completed_jo",
    )
    list_filter = ("client", "status")
    search_fields = (
        "caller_interaction_record__ticket_number",
        "client__user__first_name",
        "client__user__last_name",
        "client__client_code",
    )
    readonly_fields = ("created_at", "updated_at")


class PrepaidSubscriptionAdmin(ImportExportModelAdmin):
    model = PrepaidSubscription
    resources = resources.PrepaidSubscriptionResource
    list_display = (
        "client",
        "date_paid",
        "month_year",
        "plan_type",
        "monthly_fee",
        "payment_status",
    )
    list_filter = ("client", "payment_status", "month_year", "plan_type")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "client__client_code",
    )


class SubscriptionTypeAdmin(ImportExportModelAdmin):
    model = SubscriptionType
    resources = resources.SubscriptionTypeResource
    list_display = (
        "name",
    )
    list_filter = ("name",)
    search_fields = (
        "name",
    )


class PaymentSummaryAdmin(ImportExportModelAdmin):
    model = PaymentSummary
    resources = resources.PaymentSummaryResource
    list_display = (
        "client",
        "date_paid",
        "month_year",
        "plan_type",
        "monthly_fee",
        "payment_status",
    )
    list_filter = ("client", "payment_status", "month_year", "plan_type")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "client__client_code",
    )


admin.site.register(PaymentSummary)
admin.site.register(CustomerInteractionPrepaid, CustomerInteractionPrepaidAdmin)
admin.site.register(InteractionRecord, InteractionRecordAdmin)
admin.site.register(MinutesReport, MinutesReportAdmin)
admin.site.register(Prepaid, PrepaidAdmin)
admin.site.register(AccountCharge, AccountChargeAdmin)
admin.site.register(AccountBalance, AccountBalanceAdmin)
admin.site.register(JobOrderPrepaid, JobOrderAdmin)
admin.site.register(PrepaidSubscription, PrepaidSubscriptionAdmin)
admin.site.register(SubscriptionType, SubscriptionTypeAdmin)
