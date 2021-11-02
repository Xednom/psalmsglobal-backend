from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.vodaconnect.models import (
    VoipInformation,
    ActivationDetail,
    PlanDetail,
    SubscriberStatus,
    ForwardingInformation,
    TotalNumberOfExtension,
    ZipTrunkLogin,
    OtherLogin,
)
from apps.vodaconnect.serializers import (
    VoipInformationSerializer,
    ActivationDetailSerializer,
    PlanDetailSerializer,
    SubscriberStatusSerializer,
    ForwardingInformationSerializer,
)

User = get_user_model()


__all__ = (
    "VoipInformationViewSet",
    "ActivationDetailViewSet",
    "PlanDetailViewSet",
    "SubscriberStatusViewSet",
    "ForwardingInformationViewSet",
)


class VoipInformationViewSet(viewsets.ModelViewSet):
    serializer_class = VoipInformationSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = VoipInformation.objects.select_related("client").filter(
                client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = VoipInformation.objects.select_related("client").all()
            return qs


class ActivationDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationDetailSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = ActivationDetail.objects.select_related("client").filter(
                client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = ActivationDetail.objects.select_related("client").all()
            return qs


class PlanDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PlanDetailSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = PlanDetail.objects.select_related("client", "plan_type").filter(
                client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = PlanDetail.objects.select_related("client", "plan_type").all()
            return qs


class SubscriberStatusViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriberStatusSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = SubscriberStatus.objects.select_related("client").filter(
                client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = SubscriberStatus.objects.select_related("client").all()
            return qs


class ForwardingInformationViewSet(viewsets.ModelViewSet):
    serializer_class = ForwardingInformationSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = ForwardingInformation.objects.select_related(
                "client",
            ).filter(client__user__in=user)
            return qs
        elif current_user.is_superuser:
            qs = ForwardingInformation.objects.select_related("client").all()
            return qs
