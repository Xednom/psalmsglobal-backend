from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from apps.post_paid.models import (
    AccountBalance,
    AccountCharge,
    Acquisition,
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
    TicketSummary,
    PrepForMarketing,
    Disposition,
    OverallTagging,
    TicketSummaryComment,
    JobOrderTicketSummary
)

from apps.post_paid import resources


class TicketSummaryComment(admin.TabularInline):
    model = TicketSummaryComment
    extra = 1
    fields = ("user", "comment", "created_at", "updated_at")
    readonly_fields = ("user", "created_at", "updated_at")


class AccountBalanceAdmin(ImportExportModelAdmin):
    model = AccountBalance
    resource_class = resources.AccountBalanceResource
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
    resource_class = resources.AccountChargeResource
    list_display = ("client", "agent", "ticket_number", "date_called", "total_minutes")
    list_filter = ("client", "agent")
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "agent__user__first_name",
        "agent__user__last_name",
    )
    readonly_fields = ("created_at", "updated_at")


class CustomerInteractionPostPaidAdmin(ImportExportModelAdmin):
    model = CustomerInteractionPostPaid
    resource_class = resources.CustomerInteractionPostPaidResource
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
        "company__client",
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
        # "company",
        "company__client__user__first_name",
        "company__client__user__last_name",
        "company__client__user__username",
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

    def get_queryset(self, request):
        qs = super(CustomerInteractionPostPaidAdmin, self).get_queryset(request)
        return qs.all()


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
        "created_at",
        "id",
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


class TicketSummaryAdmin(ImportExportModelAdmin):
    model = TicketSummary
    resource_class = resources.TicketSummaryResource
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
        "acquisition_tagging",
        "prep_for_marketing",
        "disposition_tagging",
        "sales_team_assigned",
    )
    list_filter = (
        "company__company_name",
        "company__company_owner_name",
        "agent",
        "county",
        "state",
        "crm",
        "leads_transferred_crm",
        "internal_auditor",
        "interested_to_sell",
        "interested_to_buy",
        "general_call",
        "acquisition_tagging",
        "prep_for_marketing",
        "disposition_tagging",
        "sales_team_assigned",
        "overall_tagging"
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
    inlines = [TicketSummaryComment]


class AcquisitionAdmin(admin.ModelAdmin):
    model = Acquisition
    list_display = ("description",)
    search_fields = ("description", "notes", "additional_info")


class PrepForMarketingAdmin(admin.ModelAdmin):
    model = PrepForMarketing
    list_display = ("description",)
    search_fields = ("description", "notes", "additional_info")


class DispositionAdmin(admin.ModelAdmin):
    model = Disposition
    list_display = ("description",)
    search_fields = ("description", "notes", "additional_info")


class OverallTaggingAdmin(admin.ModelAdmin):
    model = OverallTagging
    list_display = ("description",)
    search_fields = ("description", "notes", "additional_info")


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
admin.site.register(TicketSummary, TicketSummaryAdmin)
admin.site.register(Acquisition, AcquisitionAdmin)
admin.site.register(PrepForMarketing, PrepForMarketingAdmin)
admin.site.register(Disposition, DispositionAdmin)
admin.site.register(OverallTagging, DispositionAdmin)
admin.site.register(JobOrderTicketSummary)