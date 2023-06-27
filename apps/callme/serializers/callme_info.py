from django.contrib.auth import get_user_model

from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.authentication.models import User, Staff, Client
from apps.callme.models import (
    Company,
    PropertyInfo,
    OfferStatus,
    PropertyFileInfo,
    CommentOfferTabAgent,
    CommentOfferTabCustomer,
    CommentOfferTabClient,
)

# User = get_user_model


__all__ = (
    "CallMeInfoSerializer",
    "OfferStatusSerializer",
    "PropertyFileSerializer",
    "CommentOfferTabAgentSerializer",
    "CommentOfferTabCustomerSerializer",
    "CommentOfferTabClientSerializer",
)


class CommentOfferTabAgentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = CommentOfferTabAgent
        fields = ("user", "property_info", "comment", "commenter")
    
    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            user = User.objects.filter(username=instance.user)
            staffs = Staff.objects.select_related("user").filter(user__in=user)
            staff_code = [staff.staff_id for staff in staffs]
            return "".join(staff_code)
        else:
            user = User.objects.filter(username=instance.user)
            clients = Client.objects.select_related("user").filter(user__in=user)
            client_code = [client.client_code for client in clients]
            return "".join(client_code)


class CommentOfferTabCustomerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = CommentOfferTabCustomer
        fields = ("created_at", "user", "property_info", "comment", "commenter")

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            user = User.objects.filter(username=instance.user)
            staffs = Staff.objects.select_related("user").filter(user__in=user)
            staff_code = [staff.staff_id for staff in staffs]
            return "".join(staff_code)
        else:
            user = User.objects.filter(username=instance.user)
            clients = Client.objects.select_related("user").filter(user__in=user)
            client_code = [client.client_code for client in clients]
            return "".join(client_code)



class CommentOfferTabClientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = CommentOfferTabClient
        fields = ("user", "property_info", "comment", "commenter")

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            user = User.objects.filter(username=instance.user)
            staffs = Staff.objects.select_related("user").filter(user__in=user)
            staff_code = [staff.staff_id for staff in staffs]
            return "".join(staff_code)
        else:
            user = User.objects.filter(username=instance.user)
            clients = Client.objects.select_related("user").filter(user__in=user)
            client_code = [client.client_code for client in clients]
            return "".join(client_code)


class OfferStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferStatus
        fields = ("name",)


class CallMeInfoSerializer(WritableNestedModelSerializer):
    property_info_comment_tab_agents = CommentOfferTabAgentSerializer(
        many=True, required=False, allow_null=True
    )
    property_info_comment_tab_clients = CommentOfferTabClientSerializer(
        many=True, required=False, allow_null=True
    )
    property_info_comment_tab_customers = CommentOfferTabCustomerSerializer(
        many=True, required=False, allow_null=True
    )

    class Meta:
        model = PropertyInfo
        fields = (
            "id",
            "client_code",
            "full_name",
            "company_name",
            "reference_number",
            "apn",
            "county",
            "state",
            "size",
            "address",
            "price",
            "due_diligence",
            "ad_content",
            "images",
            "website",
            "comment_offer_tab_customer",
            "comment_offer_tab_client",
            "comment_sales_agent_notes",
            "facebook",
            "fb_groups",
            "landmodo",
            "fsbo",
            "instagram",
            "land_listing",
            "land_flip",
            "land_hub",
            "land_century",
            "property_info_comment_tab_agents",
            "property_info_comment_tab_clients",
            "property_info_comment_tab_customers",
        )


class PropertyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyFileInfo
        fields = ("file",)
