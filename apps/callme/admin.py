from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from apps.callme.models import Company, Crm, PhoneSystem, Script, Subscription


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = (
        "company_owner_name",
        "company_name",
        "client",
        "business_type",
        "company_forwarding_email",
    )
    list_filter = ("client",)
    search_fields = (
        "company_owner_name",
        "company_name",
        "client__user__first_name",
        "client__user__last_name",
    )
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Company Information",
            {
                "fields": (
                    "client",
                    "company_owner_name",
                    "company_name",
                    "business_type",
                    "company_phone",
                    "company_email",
                    "company_complete_address",
                    "company_forwarding_email",
                    "paypal_email",
                    "notes",
                )
            },
        ),
    )


class CrmAdmin(admin.ModelAdmin):
    model = Crm
    list_display = ("company", "crm", "crm_url")
    list_filter = ("company",)
    search_fields = ("company", "client__user__first_name", "client__user__last_name")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "CRM Information",
            {
                "fields": (
                    "company",
                    "crm",
                    "type_of_crm",
                    "crm_url",
                    "crm_login",
                    "notes",
                )
            },
        ),
    )


class PhoneSystemAdmin(admin.ModelAdmin):
    model = PhoneSystem
    list_display = (
        "company",
        "sub_number",
        "caller_id_detail",
        "vodaconnect_plan",
        "original_line",
        "call_forwarding_number",
    )
    list_filter = ("vodaconnect_plan", "vodaconnect_line_type")
    search_fields = (
        "company",
        "company__client__user__first_name",
        "company__client__user__last_name",
        "sub_number",
        "original_line",
    )
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Phone System Information",
            {
                "fields": (
                    "company",
                    "sub_number",
                    "caller_id_detail",
                    "vodaconnect_plan",
                    "original_line",
                    "call_forwarding_number",
                    "vodaconnect_line_type",
                )
            },
        ),
    )


class ScriptAdmin(admin.ModelAdmin):
    model = Script
    list_display = ("company", "form", "company_address", "mailing_lists")
    list_filter = ("company",)
    search_fields = (
        "company",
        "company__client__user__first_name",
        "client__user__last_name",
        "client__client_code",
    )
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Script Information",
            {"fields": ("company", "company_address", "form", "mailing_lists")},
        ),
    )


class SubscriptionAdmin(admin.ModelAdmin):
    model = Subscription
    list_display = (
        "company",
        "signed_up_date",
        "signed_out_date",
        "biling_cycle",
        "date_call_started",
        "status",
    )
    list_filter = ("company",)
    search_fields = (
        "company",
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
                    "notes"
                )
            },
        ),
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Crm, CrmAdmin)
admin.site.register(PhoneSystem, PhoneSystemAdmin)
admin.site.register(Script, ScriptAdmin)