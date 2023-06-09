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
from apps.callme.resources import (
    FormResource,
    CompanyResource,
    PropertyInfoResource,
    StateResource,
    CountyResource,
    CrmResource,
    VodaconnectPlanResource,
    VodaconnectLineTypeResource,
    PhoneSystemResource,
)
from apps.core.admin import ModelAdminMixin


class CompanyAdmin(ImportExportModelAdmin):
    model = Company
    resource_class = CompanyResource
    list_display = (
        "client",
        "company_owner_name",
        "company_name",
        "company_phone",
        "company_email",
        "company_forwarding_email",
        "paypal_email",
    )
    list_filter = ("client", "company_owner_name", "company_name")
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


class CrmAdmin(ImportExportModelAdmin):
    model = Crm
    resource_class = CrmResource
    list_display = ("company", "crm", "crm_login", "crm_url")
    list_filter = ("company__company_name", "crm")
    search_fields = (
        "company__client__user__username",
        "company__client__user__first_name",
        "company__client__user__last_name",
    )
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


class PhoneSystemAdmin(ImportExportModelAdmin):
    model = PhoneSystem
    resource_class = PhoneSystemResource
    list_display = (
        "company",
        "sub_number",
        "caller_id_detail",
        "vodaconnect_plan",
        "original_line",
        "call_forwarding_number",
        "vodaconnect_line_type",
    )
    list_filter = (
        "company",
        "sub_number",
        "caller_id_detail",
        "vodaconnect_plan",
        "vodaconnect_line_type",
    )
    search_fields = (
        "company__client__user__first_name",
        "company__client__user__last_name",
        "original_line",
        "caller_id_detail",
        "vodaconnect_line_type__line",
        "vodaconnect_plan__range",
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
    list_filter = ("form_title", "company")
    search_fields = (
        "form_title",
        "company__company_name",
    )
    list_display = (
        "form_title",
        "company",
        "mailing_lists",
    )
    fieldsets = (
        (
            "Form Information",
            {
                "fields": (
                    "form_title",
                    "company",
                    "mailing_lists_unpacked",
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


class StateAdmin(ImportExportModelAdmin):
    model = State
    resource_class = StateResource
    list_display = ("name",)
    list_filter = ("name",)


class CountyAdmin(ImportExportModelAdmin):
    model = County
    resource_class = CountyResource
    list_display = ("name", "state")
    list_filter = ("name", "state")


class VodaconnectLineTypeAdmin(ImportExportModelAdmin):
    model = VodaconnectLineType
    resource_class = VodaconnectLineTypeResource
    list_display = ("line",)
    list_filter = ("line",)


class VodaconnectPlanAdmin(ImportExportModelAdmin):
    model = VodaconnectPlan
    resource_class = VodaconnectPlanResource
    list_display = ("range",)
    list_filter = ("range",)


class PropertyInfoAdmin(ImportExportModelAdmin):
    model = PropertyInfo
    resource_class = PropertyInfoResource
    list_display = (
        "company_name",
        "apn",
        "reference_number",
        "address",
    )
    list_filter = (
        "company_name",
    )
    search_fields = ("company__company_name",)
    fieldsets = (
        (
            "Property info",
            {
                "fields": (
                    "client_code",
                    "full_name",
                    "company_name",
                    "reference_number",
                    "apn",
                    "county",
                    "state",
                    "size",
                    "address",
                    "price",
                    "due_diligence",
                    "ad_content",
                    "images",
                    "website",
                    "comment_offer_tab_customer",
                    "comment_offer_tab_client",
                    "comment_sales_agent_notes",
                    "facebook",
                    "fb_groups",
                    "landmodo",
                    "fsbo",
                    "instagram",
                    "land_listing",
                    "land_flip",
                    "land_hub",
                    "land_century",
                )
            },
        ),
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Crm, CrmAdmin)
admin.site.register(PhoneSystem, PhoneSystemAdmin)
admin.site.register(VodaconnectLineType, VodaconnectLineTypeAdmin)
admin.site.register(VodaconnectPlan, VodaconnectPlanAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(PropertyInfo, PropertyInfoAdmin)
admin.site.register(OfferStatus)
