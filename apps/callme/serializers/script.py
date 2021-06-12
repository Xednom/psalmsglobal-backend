from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.callme.models import Form, Attribute, Script, Company


__all__ = ("FormSerializer", "ScriptSerializer")


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ("form", "data_type", "value_text", "value_question")


class FormSerializer(WritableNestedModelSerializer):
    attribute_forms = AttributeSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Form
        fields = ("id", "form_title", "company", "attribute_forms")


class ScriptSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
    )
    form = serializers.SlugRelatedField(
        slug_field="form_title",
        queryset=Form.objects.all(),
        allow_null=True,
        required=False,
    )
    mailing_lists = serializers.JSONField()

    class Meta:
        model = Script
        fields = (
            "id",
            "company",
            "company_address",
            "form",
            "status",
            "mailing_lists",
        )
