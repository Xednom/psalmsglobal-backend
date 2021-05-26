from rest_framework import serializers

from apps.callme.models import AttributeType, Form, Script


__all__ = ("AttributeTypeSerializer", "FormSerializer", "ScriptSerializer")


class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeType
        fields = ("text", "question")


class FormSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(
        queryset=AttributeType.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Form
        fields = ("form_title", "attribute", "value_text", "value_question")


class ScriptSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Script.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Script
        fields = ("company", "company_address", "form", "mailing_lists")
