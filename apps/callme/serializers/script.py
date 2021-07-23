from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.callme.models import Form, Attribute, Script, Company


__all__ = ("AttributeSerializer", "FormSerializer", "ScriptSerializer")


class AttributeSerializer(serializers.ModelSerializer):
    form_id = serializers.SerializerMethodField()

    class Meta:
        model = Attribute
        fields = (
            "form_id",
            "data_type",
            "value_text",
            "value_question",
            "input_question",
        )

    def get_form_id(self, instance):
        return f"{instance.form.id}"


class FormSerializer(WritableNestedModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field="company_name",
        queryset=Company.objects.all(),
        required=False,
        allow_null=True,
    )
    attribute_forms = AttributeSerializer(many=True, required=False, allow_null=True)
    id_form = serializers.SerializerMethodField()
    mailing_lists = serializers.JSONField()

    class Meta:
        model = Form
        fields = (
            "id",
            "id_form",
            "form_title",
            "company",
            "attribute_forms",
            "original_script",
            "mailing_lists",
            "status"
        )

    def get_id_form(self, instance):
        return f"{instance.id}"


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
