from import_export import resources
from apps.account.models import LoginCredential, AccountFile


class LoginCredentialResource(resources.ModelResource):
    class Meta:
        model = LoginCredential
        fields = "client" "category" "url" "username" "password" "notes" "staff"


class AccountFileResource(resources.ModelResource):
    class Meta:
        model = AccountFile
        fields = "client" "file_name" "url" "file_description" "staff"
