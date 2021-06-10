from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import Crm, Company
from apps.callme.serializers import CrmSerializer

User = get_user_model()


__all__ = ("CrmViewSet",)


class CrmViewSet(viewsets.ModelViewSet):
    serializer_class = CrmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        users = User.objects.filter(username=current_user)
        user = users.all()

        if current_user:
            queryset = Crm.objects.select_related("company").filter(
                company__client__user__in=user
            )
            return queryset
        elif current_user.is_superuser:
            qs = Crm.objects.select_related("company").all()
            return qs
