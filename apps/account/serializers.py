from rest_framework import serializers

from apps.authentication.models import Client, Staff
from apps.account.models import LoginCredential, AccountFile


class LoginCredentialSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = LoginCredential
        fields = (
            "id",
            "client",
            "category",
            "url",
            "username",
            "password",
            "notes",
            "staff",
        )


class AccountFileSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = AccountFile
        fields = (
            "id",
            "client",
            "file_name",
            "url",
            "file_description",
            "staff",
        )
