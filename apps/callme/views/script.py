from django.contrib.auth import get_user, get_user_model

from django_filters import CharFilter
from django_filters import rest_framework as filters
from rest_framework import generics, viewsets, permissions

from apps.authentication.models import Client
from apps.callme.models import Form, Script, Company
from apps.callme.serializers import (
    ScriptSerializer,
    FormSerializer,
)

User = get_user_model()


__all__ = ("FormViewSet", "ScriptViewSet", "FormView")


class FormView(generics.RetrieveAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class FormFilter(filters.FilterSet):
    company = CharFilter(field_name="company__company_name", lookup_expr="startswith")

    class Meta:
        model = Form
        fields = ("company",)


class FormViewSet(viewsets.ModelViewSet):
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FormFilter

    def get_queryset(self):
        current_user = self.request.user
        users = User.objects.filter(username=current_user)
        user = users.all()

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = Form.objects.select_related(
                "company", "customer_interaction_post_paid"
            ).filter(company__client__user__in=user, original_script=True)
            return qs
        elif current_user.designation_category == "staff":
            qs = Form.objects.select_related(
                "company", "customer_interaction_post_paid"
            ).filter(original_script=True, status=True)
            return qs
        else:
            qs = Form.objects.all()
            return qs


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
