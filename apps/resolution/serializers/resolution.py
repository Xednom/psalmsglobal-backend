from rest_framework import serializers

from apps.authentication.models import Client
from apps.resolution.models import Resolution, ResolutionConversation
from apps.core.models import ResolutionCategory


__all__ = ("ResolutionSerializer", "ResolutionConversationSerializer", "ResolutionCategorySerializer")


class ResolutionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionCategory
        fields = ("id", "name")


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

    class Meta:
        model = Resolution
        fields = (
            "id",
            "category",
            "description",
            "assigned_to",
            "client",
            "status",
        )


class ResolutionConversationSerializer(serializers.ModelSerializer):
    resolution = serializers.PrimaryKeyRelatedField(
        queryset=Resolution.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = ResolutionConversation
        fields = (
            "id",
            "resolution",
            "user",
            "comment",
        )
