from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.callme.models import CallMeInfo, callme_info
from apps.callme.serializers import CallMeInfoSerializer

User = get_user_model()


__all__ = ("CallMeInfoViewSet",)


class CallMeInfoViewSet(viewsets.ModelViewSet):
    queryset = CallMeInfo.objects.select_related("company").all()
    serializer_class = CallMeInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["=apn", "=reference"]
