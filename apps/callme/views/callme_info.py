from django.contrib.auth import get_user, get_user_model

from django_filters import CharFilter
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions

from apps.callme.models import PropertyInfo, OfferStatus
from apps.callme.serializers import CallMeInfoSerializer, OfferStatusSerializer

User = get_user_model()


__all__ = ("CallMeInfoViewSet", "OfferStatusViewSet")


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
    filterset_class = (CallMeInfoFilter)
