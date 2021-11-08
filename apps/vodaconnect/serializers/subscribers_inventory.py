from apps.vodaconnect.models.active_plan_detail import PlanType
from rest_framework import serializers

from apps.vodaconnect.models import (
    VoipInformation,
    ActivationDetail,
    PlanDetail,
    SubscriberStatus,
    ForwardingInformation,
    TotalNumberOfExtension,
    ZipTrunkLogin,
    OtherLogin,
)
from apps.authentication.models import Client


__all__ = (
    "VoipInformationSerializer",
    "ActivationDetailSerializer",
    "PlanDetailSerializer",
    "SubscriberStatusSerializer",
    "TotalNumberOfExtensionSerializer",
    "ZipTrunkLoginSerializer",
    "OtherLoginSerializer",
    "ForwardingInformationSerializer",
)


class VoipInformationSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = VoipInformation
        fields = ("vodaconnect_number", "client", "client_code", "company_name")


class ActivationDetailSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = ActivationDetail
        fields = (
            "client",
            "order_request_date",
            "request_date_initiated",
            "date_line_activated",
            "date_line_terminated",
            "phone_line_status",
            "client_company_user_category",
        )


class PlanDetailSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    plan_type = serializers.SlugRelatedField(
        slug_field="name",
        queryset=PlanType.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = PlanDetail
        fields = (
            "client",
            "plan_type",
            "total_cost",
            "recurring_bill",
            "paypal_details_for_billing",
            "due_date",
        )


class SubscriberStatusSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = SubscriberStatus
        fields = ("client", "status_in_production", "type_of_request", "testimony")


class TotalNumberOfExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalNumberOfExtension
        fields = (
            "forwarding_information",
            "extension_number",
            "extension_logins",
            "notes",
        )


class ZipTrunkLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipTrunkLogin
        fields = (
            "forwarding_information",
            "zip_trunk_details",
            "notes",
        )


class OtherLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherLogin
        fields = (
            "forwarding_information",
            "description",
            "notes",
        )


class ForwardingInformationSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    forwarding_information_total_number_of_extensions = (
        TotalNumberOfExtensionSerializer(many=True, required=False, allow_null=True)
    )
    forwarding_information_zip_trunk_logins = ZipTrunkLoginSerializer(
        many=True, required=False, allow_null=True
    )
    forwarding_information_other_logins = OtherLoginSerializer(
        many=True, required=False, allow_null=True
    )

    class Meta:
        model = ForwardingInformation
        fields = (
            "id",
            "client",
            "forwarding_number",
            "notes",
            "forwarding_information_total_number_of_extensions",
            "forwarding_information_zip_trunk_logins",
            "forwarding_information_other_logins",
        )
