from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.callme.models import (
    PhoneSystem,
    Company,
    VodaconnectPlan,
    VodaconnectLineType,
)
from apps.callme.serializers import (
    PhoneSystemSerializer,
    VodaconnectPlanSerializer,
    VodaconnectLineTypeSerializer,
)

User = get_user_model()


__all__ = ("PhoneSystemViewSet", "VodaconnectPlanViewSet", "VodaconnectLineTypeViewSet")


class PhoneSystemViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneSystemSerializer
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
            qs = PhoneSystem.objects.select_related("company").filter(
                company__client__user__in=user
            )
            return qs


class VodaconnectPlanViewSet(viewsets.ModelViewSet):
    serializer_class = VodaconnectPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = VodaconnectPlan.objects.all()


class VodaconnectLineTypeViewSet(viewsets.ModelViewSet):
    serializer_class = VodaconnectLineTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = VodaconnectLineType.objects.all()
