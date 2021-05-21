from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.contrib.auth import get_user_model
from .models import Client, Staff

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserListSerializer


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "designation_category",
            "company_category",
        )


class UserListSerializer(BaseUserListSerializer):
    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "email",
            "phone",
            "designation_category",
            "company_category",
        )


class ClientSerializer(WritableNestedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    client_hourly_rate = serializers.CharField(source="hourly_rate", required=False, allow_null=True)

    class Meta:
        model = Client
        fields = (
            "id",
            "user",
            "client_code",
            "hourly_rate",
            "client_hourly_rate",
            "affiliate_partner_code",
            "affiliate_partner_name",
            "pin",
            "lead_information",
            "customer_id",
        )


class ClientCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("client_code", "hourly_rate")


class StaffSerializer(WritableNestedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.all(), required=False, allow_null=True
    )
    start_date_hired = serializers.DateField(
        format="%Y-%m-%d",
        input_formats=[
            "%Y-%m-%d",
        ],
        allow_null=True,
        required=False,
    )
    date_hired_in_contract = serializers.DateField(
        format="%Y-%m-%d",
        input_formats=[
            "%Y-%m-%d",
        ],
        allow_null=True,
        required=False,
    )

    class Meta:
        model = Staff
        fields = (
            "id",
            "user",
            "date_of_birth",
            "blood_type",
            "position",
            "company_id",
            "staff_id",
            "phone_number",
            "company_email",
            "start_date_hired",
            "date_hired_in_contract",
            "base_pay",
            "hourly_rate",
            "status",
            "category",
            "residential_address",
            "tin_number",
            "sss_number",
            "pag_ibig_number",
            "phil_health_number",
            "emergency_contact_full_name",
            "relationship",
            "emergency_contact_number",
            "mothers_full_name",
            "mothers_maiden_name",
            "fathers_full_name",
            "bank_name",
            "bank_account_name",
            "bank_type",
            "bank_account_number",
        )


class CurrentUserSerializer(BaseUserListSerializer, WritableNestedModelSerializer):
    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "phone",
            "first_name",
            "last_name",
            "designation_category",
            "company_category",
        )
