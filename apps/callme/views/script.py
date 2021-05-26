from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import AttributeType, Form, Script, Company
from apps.callme.serializers import (
    ScriptSerializer,
    AttributeTypeSerializer,
    FormSerializer,
)

User = get_user_model()


__all__ = ("AttributeTypeViewSet", "FormViewSet", "ScriptViewSet")


class AttributeTypeViewSet(viewsets.ModelViewSet):
    serializer_class = AttributeTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = AttributeType.objects.all()


class FormViewSet(viewsets.ModelViewSet):
    serialzer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Form.objects.all()


class ScriptViewSet(viewsets.ModelViewSet):
    serializer_class = ScriptSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user_company = Company.objects.select_related("client").filter(
            client__user=current_user
        )

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = Script.objects.select_related("company").filter(company=user_company)
            return qs
        elif current_user.designation_category == "staff":
            qs = Script.objects.all()
            return qs
