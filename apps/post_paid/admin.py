from django.contrib import admin

from apps.post_paid.models import (
    AccountBalance,
    AccountCharge,
    InterestedToBuy,
    InterestedToSell,
    GeneralCall,
    CustomerInteractionPostPaid,
    InteractionRecord,
    MinutesReport,
    MonthlyCharge,
    PlanType,
    CostPlan,
    PostPaid,
    Subscription,
    JobOrderPostPaid,
    InternalAuditor,
)


class AccountBalanceAdmin(admin.ModelAdmin):
    model = AccountBalance
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


class AccountChargeAdmin(admin.ModelAdmin):
    model = AccountCharge
    list_display = ("client", "agent", "ticket_number", "date_called", "total_minutes")
    list_filter = ("client", "agent")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "agent__user__first_name",
        "agent__user__last_name",
    )
    readonly_fields = ("created_at", "updated_at")


class CustomerInteractionPostPaidAdmin(admin.ModelAdmin):
    model = CustomerInteractionPostPaid
    list_display = (
        "ticket_number",
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
        "company",
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


class InteractionRecordAdmin(admin.ModelAdmin):
    model = InteractionRecord
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


class MinutesReportAdmin(admin.ModelAdmin):
    model = MinutesReport
    list_display = (
        "client",
        "month_year",
        "plan_type",
        "cost_of_plan",
        "plan_allocated_minutes",
        "ci_minutes_overview",
        "general_request_total_minutes",
        "monthly_usage",
        "total_minutes_unused",
    )
    list_filter = ("client", "month_year", "cost_of_plan", "plan_allocated_minutes")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "month_year",
        "cost_of_plan",
        "plan_allocated_minutes",
    )
    readonly_fields = ("created_at", "updated_at")


class MonthlyChargeAdmin(admin.ModelAdmin):
    model = MonthlyCharge
    list_display = (
        "client",
        "month_year",
        "plan_type",
        "total_minutes",
        "cost_of_plan",
        "payment_reference",
        "payment_status",
        "date_paid",
    )
    list_filter = ("client", "month_year", "payment_status", "plan_type")
    search_fields = (
        "client__client_code",
        "client__user__first_name",
        "client__user__last_name",
        "month_year",
    )
    readonly_fields = ("created_at", "updated_at")


class PlanTypeAdmin(admin.ModelAdmin):
    model = PlanType
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class CostPlanAdmin(admin.ModelAdmin):
    model = CostPlan
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class InterestedToBuyAdmin(admin.ModelAdmin):
    model = InterestedToBuy
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class InterestedToSellAdmin(admin.ModelAdmin):
    model = InterestedToSell
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class GeneralCallAdmin(admin.ModelAdmin):
    model = GeneralCall
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")


class PostPaidAdmin(admin.ModelAdmin):
    model = PostPaid
    list_display = (
        "client",
        "plan_type",
        "total_minutes",
        "cost_of_plan",
        "start_of_plan",
        "end_of_plan",
        "account_status",
        "recurring_bill",
    )
    list_filter = ("client", "account_status", "recurring_bill")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name" "plan_type__name",
    )
    readonly_fields = ("created_at", "updated_at")


class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = (
        "company",
        "signed_up_date",
        "signed_out_date",
        "billing_cycle",
        "date_call_started",
        "status",
    )
    list_filter = ("company", "status")
    search_fields = (
        "company__company_name",
        "company__client__user__first_name",
        "client__user__last_name",
        "client__client_code",
    )
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Subscription Information",
            {
                "fields": (
                    "company",
                    "signed_up_date",
                    "signed_out_date",
                    "billing_cycle",
                    "date_call_started",
                    "status",
                    "script_created",
                    "notes",
                )
            },
        ),
    )


class JobOrderAdmin(admin.ModelAdmin):
    model = JobOrderPostPaid
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
    # fieldsets = (
    #     (
    #         "Subscription Information",
    #         {
    #             "fields": (
    #                 "company",
    #                 "signed_up_date",
    #                 "signed_out_date",
    #                 "billing_cycle",
    #                 "date_call_started",
    #                 "status",
    #                 "script_created",
    #                 "notes"
    #             )
    #         },
    #     ),
    # )


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(CustomerInteractionPostPaid, CustomerInteractionPostPaidAdmin)
admin.site.register(InteractionRecord, InteractionRecordAdmin)
admin.site.register(MinutesReport, MinutesReportAdmin)
admin.site.register(MonthlyCharge, MonthlyChargeAdmin)
admin.site.register(PostPaid, PostPaidAdmin)
admin.site.register(PlanType, PlanTypeAdmin)
admin.site.register(CostPlan, CostPlanAdmin)
admin.site.register(InterestedToSell, InterestedToSellAdmin)
admin.site.register(InterestedToBuy, InterestedToBuyAdmin)
admin.site.register(AccountCharge, AccountChargeAdmin)
admin.site.register(AccountBalance, AccountBalanceAdmin)
admin.site.register(GeneralCall, GeneralCallAdmin)
admin.site.register(JobOrderPostPaid, JobOrderAdmin)
admin.site.register(InternalAuditor)
