from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import (
    User,
    Client,
    Staff,
)
from apps.authentication.resources import ClientResource, StaffResource, UserResource

from import_export.admin import ImportExportModelAdmin

User = get_user_model()


class UserProfileAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "designation_category",
        "company_category",
        "account_type",
        "is_staff",
    )
    list_filter = (
        "designation_category",
        "company_category",
        "first_name",
        "last_name",
        "account_type",
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
    )
    search_fields = (
        "first_name",
        "last_name",
        "account_type",
        "company_category",
        "designation_category",
    )
    UserAdmin.fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal Informations"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "designation_category",
                    "company_category",
                    "account_type",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class ClientProfileAdmin(ImportExportModelAdmin):
    model = Client
    resource_class = ClientResource
    list_display = (
        "get_user",
        "client_code",
        "get_email",
        "affiliate_partner_name",
        "affiliate_partner_code",
        "hourly_rate",
        "customer_id",
    )
    list_filter = (
        "affiliate_partner_code",
        "affiliate_partner_name",
        "user",
    )
    search_fields = (
        "affiliate_partner_name",
        "affiliate_partner_code",
        "user__first_name",
        "user__username",
        "user__last_name",
        "client_code",
    )
    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "user",
                    "client_code",
                    "affiliate_partner_code",
                    "affiliate_partner_name",
                    "hourly_rate",
                    "pin",
                    "lead_information",
                    "customer_id",
                )
            },
        ),
    )

    def get_user(self, obj):
        return obj.user.user_full_name

    get_user.admin_order_field = "user__first_name"
    get_user.short_description = "Client name"

    def get_email(self, obj):
        return obj.user.email

    get_email.admin_order_field = "user__email"
    get_email.short_description = "User email"


class StaffProfileAdmin(ImportExportModelAdmin):
    model = Staff
    resource_class = StaffResource
    list_display = (
        "get_user",
        "get_email",
        "date_of_birth",
        "phone_number",
        "date_hired_in_contract",
        "staff_id",
        "company_id",
    )
    list_filter = ("user", "position", "status", "category")
    search_fields = ("user__first_name", "user__last_name", "user__username")
    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "user",
                    "date_of_birth",
                    "blood_type",
                    "position",
                    "phone_number",
                    "company_email",
                    "start_date_hired",
                    "date_hired_in_contract",
                    "base_pay",
                    "hourly_rate",
                    "status",
                    "category",
                    "residential_address",
                    "company_id",
                    "staff_id",
                )
            },
        ),
        (
            "Government Information",
            {
                "fields": (
                    "tin_number",
                    "sss_number",
                    "pag_ibig_number",
                    "phil_health_number",
                )
            },
        ),
        (
            "Emergency Information",
            {
                "fields": (
                    "emergency_contact_full_name",
                    "relationship",
                    "emergency_contact_number",
                    "mothers_full_name",
                    "mothers_maiden_name",
                    "fathers_full_name",
                )
            },
        ),
        (
            "Payroll Information",
            {
                "fields": (
                    "bank_name",
                    "bank_account_name",
                    "bank_type",
                    "bank_account_number",
                )
            },
        ),
    )

    def get_user(self, obj):
        return obj.user.user_full_name

    get_user.admin_order_field = "user__first_name"
    get_user.short_description = "Staff name"

    def get_email(self, obj):
        return obj.user.email

    get_email.admin_order_field = "user__email"
    get_email.short_description = "Staff email"


admin.site.register(User, UserProfileAdmin)
admin.site.register(Client, ClientProfileAdmin)
admin.site.register(Staff, StaffProfileAdmin)
