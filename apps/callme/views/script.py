from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import Form, Script, Company
from apps.callme.serializers import (
    ScriptSerializer,
    FormSerializer,
)

User = get_user_model()


__all__ = ("FormViewSet", "ScriptViewSet")


class FormViewSet(viewsets.ModelViewSet):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Form.objects.all()


class ScriptViewSet(viewsets.ModelViewSet):
    serializer_class = ScriptSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        users = User.objects.filter(username=current_user)
        user = users.all()

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = Script.objects.select_related("company").filter(
                company__client__user__in=user
            )
            return qs
        elif current_user.designation_category == "staff":
            qs = Script.objects.all()
            return qs
        else:
            qs = Script.objects.all()
            return qs
