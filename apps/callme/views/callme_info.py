from django.contrib.auth import get_user, get_user_model

from django_filters import CharFilter
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions

from apps.callme.models import PropertyInfo, OfferStatus
from apps.callme.serializers import CallMeInfoSerializer, OfferStatusSerializer

User = get_user_model()


__all__ = ("CallMeInfoViewSet", "OfferStatusViewSet", "PropertyInfoViewSet")


class OfferStatusViewSet(viewsets.ModelViewSet):
    queryset = OfferStatus.objects.all()
    serializer_class = OfferStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class CallMeInfoFilter(filters.FilterSet):
    apn = CharFilter(field_name="apn", lookup_expr="icontains")
    reference = CharFilter(field_name="reference", lookup_expr="icontains")
    company_name = CharFilter(field_name="company_name", lookup_expr="icontains")

    class Meta:
        model = PropertyInfo
        fields = ("apn", "reference", "company_name")


class CallMeInfoViewSet(viewsets.ModelViewSet):
    queryset = PropertyInfo.objects.select_related("company").all()
    serializer_class = CallMeInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CallMeInfoFilter


class PropertyInfoViewSet(viewsets.ModelViewSet):
    serializer_class = CallMeInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = PropertyInfo.objects.select_related("company", "offer_status").filter(
                company__client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = PropertyInfo.objects.all()
            return qs
