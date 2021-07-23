from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from import_export.admin import ImportExportModelAdmin

from apps.callme.models import (
    Company,
    Crm,
    PhoneSystem,
    Script,
    Form,
    Attribute,
    VodaconnectPlan,
    VodaconnectLineType,
    State,
    County,
    PropertyInfo,
    OfferStatus,
)
from apps.callme.resources import FormResource
from apps.core.admin import ModelAdminMixin


class CompanyAdmin(admin.ModelAdmin):
    model = Company
    list_display = (
        "client",
        "company_owner_name",
        "company_name",
        "company_phone",
        "company_email",
        "company_forwarding_email",
        "paypal_email",
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
        "vodaconnect_line_type",
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


class AttributeAdmin(admin.TabularInline):
    model = Attribute
    extra = 1
    fields = ("form", "data_type", "value_text", "value_question", "input_question")
    readonly_fields = ("created_at", "updated_at")


class FormAdmin(ModelAdminMixin, ImportExportModelAdmin):
    model = Form
    resource_class = FormResource
    list_display = (
        "form_title",
        "company",
        "customer_interaction_post_paid",
    )
    fieldsets = (
        (
            "Form Information",
            {
                "fields": (
                    "form_title",
                    "company",
                    "customer_interaction_post_paid",
                )
            },
        ),
    )
    inlines = [AttributeAdmin]

    def get_queryset(self, request):
        qs = Form.objects.all()
        if request.user.is_superuser:
            return qs.filter(original_script=True)


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


admin.site.register(Company, CompanyAdmin)
admin.site.register(Crm, CrmAdmin)
admin.site.register(PhoneSystem, PhoneSystemAdmin)
admin.site.register(VodaconnectLineType)
admin.site.register(VodaconnectPlan)
admin.site.register(Script, ScriptAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(State)
admin.site.register(County)
admin.site.register(PropertyInfo)
admin.site.register(OfferStatus)
