from rest_framework import viewsets, permissions, generics, filters, status

from apps.callme.models import State, County
from apps.callme.serializers import StateSerializer, CountySerializer


__all__ = ("StateViewSet", "CountyViewSet")


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]
    queryset = State.objects.all()


class CountyViewSet(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]
    queryset = County.objects.select_related("state").all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["state__name"]
