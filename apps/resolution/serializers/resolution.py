from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.authentication.models import Client, Staff
from apps.resolution.models import Resolution, ResolutionConversation
from apps.core.models import ResolutionCategory


User = get_user_model()


__all__ = (
    "ResolutionSerializer",
    "ResolutionConversationSerializer",
    "ResolutionCategorySerializer",
)


class ResolutionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionCategory
        fields = ("id", "name")


class ResolutionConversationSerializer(serializers.ModelSerializer):
    resolution = serializers.PrimaryKeyRelatedField(
        queryset=Resolution.objects.all(), required=False, allow_null=True
    )
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
    )
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = ResolutionConversation
        fields = (
            "id",
            "resolution",
            "user",
            "comment",
            "commenter",
            "created_at",
        )

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


class ResolutionSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=ResolutionCategory.objects.all(),
        allow_null=True,
        required=False,
    )
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    resolution_conversations = ResolutionConversationSerializer(
        many=True, required=False, allow_null=True
    )

    class Meta:
        model = Resolution
        fields = (
            "id",
            "category",
            "description",
            "assigned_to",
            "client",
            "status",
            "resolution_conversations",
        )
