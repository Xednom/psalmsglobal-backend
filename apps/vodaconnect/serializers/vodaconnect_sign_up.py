from rest_framework import serializers

from apps.authentication.models import Client
from apps.vodaconnect.models import VodaconnectSignUp


__all__ = ("VodaconnectSignUpSerializer",)


class VodaconnectSignUpSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    client_name = serializers.CharField(
        source="client.user.user_full_name", read_only=True
    )

    class Meta:
        model = VodaconnectSignUp
        fields = ("client", "client_name", "file_description", "url")
