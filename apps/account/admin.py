from django.contrib import admin

from .models import LoginCredential, AccountFile

from apps.account.resources import LoginCredentialResource, AccountFileResource

from import_export.admin import ImportExportModelAdmin


class LoginCredentialAdmin(ImportExportModelAdmin):
    model = LoginCredential
    resource_class = LoginCredentialResource
    list_display = ("client", "get_staffs", "category", "url")
    list_filter = ("client", "staff", "category")
    filter_horizontal = ("staff",)
    search_fields = (
        "client__user__first_name",
        "client__user__last_name",
        "category",
        "username",
    )

    fieldsets = (
        (
            "Login Credentials Information",
            {
                "fields": (
                    "client",
                    "staff",
                    "category",
                    "url",
                    "username",
                    "password",
                    "notes",
                )
            },
        ),
    )

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.staff.all()])

    get_staffs.short_description = "Staffs"


class AccountFileAdmin(ImportExportModelAdmin):
    model = AccountFile
    resource_class = AccountFileResource
    list_display = ("client", "get_staffs", "file_name", "url")
    list_filter = ("staff", "client", "file_name")
    filter_horizontal = ("staff",)
    search_fields = ("client__user__first_name", "client__user__last_name", "file_name")

    def get_staffs(self, obj):
        return ", ".join([staff.staff_name for staff in obj.staff.all()])

    get_staffs.short_description = "Staffs"


admin.site.register(LoginCredential, LoginCredentialAdmin)
admin.site.register(AccountFile, AccountFileAdmin)
