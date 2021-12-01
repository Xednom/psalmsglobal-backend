from django.contrib import admin

from apps.vodaconnect.models import (
    ActivePlanDetail,
    OtherCharge,
    PlanSummaryAndPayment,
    VoipInformation,
    ActivationDetail,
    PlanDetail,
    PlanType,
    SubscriberStatus,
    ForwardingInformation,
    TotalNumberOfExtension,
    ZipTrunkLogin,
    OtherLogin,
    VodaconnectSignUp
)


class ActivePlanDetailAdmin(admin.ModelAdmin):
    model = ActivePlanDetail
    list_display = (
        "client",
        "plan_type",
        "total_minutes_included",
        "cost_of_plan",
        "start_of_plan",
        "end_of_plan",
        "account_status",
        "recurring_bill",
    )
    list_filter = (
        "client",
        "plan_type",
        "cost_of_plan",
        "account_status",
        "recurring_bill",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "plan_type__name",
    )


class OtherChargeAdmin(admin.ModelAdmin):
    model = OtherCharge
    list_display = (
        "date",
        "client",
        "vodaconnect_number",
        "type_charge",
        "amount",
        "payment_reference",
        "payment_status",
    )
    list_filter = (
        "client",
        "type_charge",
        "payment_status",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "vodaconnect_number",
        "payment_reference",
    )


class PlanSummaryAndPaymentAdmin(admin.ModelAdmin):
    model = PlanSummaryAndPayment
    list_display = (
        "created_at",
        "date_of_paid",
        "client",
        "month_year",
        "plan_type",
        "total_minutes",
        "cost_of_plan",
        "payment_reference",
        "status",
    )
    list_filter = (
        "client",
        "month_year",
        "status",
        "plan_type",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "month_year",
        "plan_type",
        "payment_reference",
        "date_of_paid",
    )


class VoipInformationAdmin(admin.ModelAdmin):
    model = VoipInformation
    list_display = (
        "vodaconnect_number",
        "client",
        "client_code",
        "company_name",
    )
    list_filter = (
        "client",
        "vodaconnect_number",
        "company_name",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "client_code",
        "vodaconnect_number",
    )


class ActivationDetailAdmin(admin.ModelAdmin):
    model = ActivationDetail
    list_display = (
        "client",
        "order_request_date",
        "request_date_initiated",
        "date_line_activated",
        "date_line_terminated",
        "phone_line_status",
        "client_company_user_category",
    )
    list_filter = (
        "client",
        "phone_line_status",
        "client_company_user_category",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "phone_line_status",
        "client_company_user_category",
    )


class PlanDetailAdmin(admin.ModelAdmin):
    model = PlanDetail
    list_display = (
        "due_date",
        "client",
        "plan_type",
        "total_cost",
        "recurring_bill",
    )
    list_filter = (
        "client",
        "plan_type",
        "recurring_bill",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "plan_type__name",
    )


class SubscriberStatusAdmin(admin.ModelAdmin):
    model = SubscriberStatus
    list_display = (
        "client",
        "status_in_production",
        "type_of_request",
        "testimony",
    )
    list_filter = (
        "client",
        "type_of_request",
        "testimony",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "status_in_production",
        "type_of_request",
        "testimony",
    )


class VodaconnectSignUpAdmin(admin.ModelAdmin):
    model = VodaconnectSignUp
    list_display = (
        "client",
        "file_description",
        "url",
    )
    list_filter = (
        "client",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "url",
    )


class ZipTrunkLoginAdmin(admin.TabularInline):
    model = ZipTrunkLogin
    extra = 1
    fields = ("zip_trunk_details", "notes")


class OtherLoginAdmin(admin.TabularInline):
    model = OtherLogin
    extra = 1
    fields = ("description", "notes")


class TotalNumberOfExtensionAdmin(admin.TabularInline):
    model = TotalNumberOfExtension
    extra = 1
    fields = ("extension_number", "extension_logins", "notes")


class ForwardingInformationAdmin(admin.ModelAdmin):
    model = ForwardingInformation
    list_display = (
        "client",
        "forwarding_number",
        "notes",
    )
    list_filter = (
        "client",
    )
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "forwarding_number",
    )
    inlines = [TotalNumberOfExtensionAdmin, OtherLoginAdmin, ZipTrunkLoginAdmin]


admin.site.register(ActivePlanDetail, ActivePlanDetailAdmin)
admin.site.register(OtherCharge, OtherChargeAdmin)
admin.site.register(PlanSummaryAndPayment, PlanSummaryAndPaymentAdmin)
admin.site.register(VoipInformation, VoipInformationAdmin)
admin.site.register(ActivationDetail, ActivationDetailAdmin)
admin.site.register(PlanDetail, PlanDetailAdmin)
admin.site.register(PlanType)
admin.site.register(SubscriberStatus, SubscriberStatusAdmin)
admin.site.register(ForwardingInformation, ForwardingInformationAdmin)
admin.site.register(VodaconnectSignUp, VodaconnectSignUpAdmin)