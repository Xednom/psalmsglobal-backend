from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import Company
from apps.callme.serializers import CompanySerializer

User = get_user_model()


__all__ = ("CompanyViewSet",)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["company_name"]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = Company.objects.select_related("client").filter(client__user__in=user)
            return qs
        elif current_user.designation_category == "staff":
            qs = Company.objects.all()
            return qs
        elif current_user.is_superuser:
            qs = Company.objects.all()
            return qs
