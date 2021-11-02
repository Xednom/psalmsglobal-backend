from rest_framework import serializers

from apps.vodaconnect.models import VodaconnectSignUp


__all__ = ("VodaconnectSignUpSerializer",)


class VodaconnectSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = VodaconnectSignUp
        fields = ("file_description", "url")
