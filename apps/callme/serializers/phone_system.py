from rest_framework import serializers

from apps.callme.models import (
    Company,
    PhoneSystem,
    VodaconnectPlan,
    VodaconnectLineType,
)


__all__ = (
    "PhoneSystemSerializer",
    "VodaconnectPlanSerializer",
    "VodaconnectLineTypeSerializer",
)


class PhoneSystemSerializer(serializers.ModelSerializer):
    client_code = serializers.CharField(
        source="company.client.client_code", required=False, allow_null=False
    )
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
    )
    vodaconnect_plan = serializers.SlugRelatedField(
        slug_field="range", queryset=VodaconnectPlan.objects.all()
    )
    vodaconnect_line_type = serializers.SlugRelatedField(
        slug_field="line", queryset=VodaconnectLineType.objects.all()
    )

    class Meta:
        model = PhoneSystem
        fields = (
            "id",
            "client_code",
            "company",
            "sub_number",
            "caller_id_detail",
            "vodaconnect_plan",
            "original_line",
            "call_forwarding_number",
            "vodaconnect_line_type",
        )


class VodaconnectPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = VodaconnectPlan
        fields = ("range",)


class VodaconnectLineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VodaconnectLineType
        fields = ("line",)
