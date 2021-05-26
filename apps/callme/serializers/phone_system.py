from rest_framework import serializers

from apps.callme.models import PhoneSystem


__all__ = ("PhoneSystemSerializer",)


class PhoneSystemSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=PhoneSystem.objects.all(), required=False, allow_null=True
    )
    
    class Meta:
        model = PhoneSystem
        fields = (
            "company",
            "sub_number",
            "caller_id_detail",
            "vodaconnect_plan",
            "original_line",
            "call_forwarding_number",
            "vodaconnect_line_type"
        )
