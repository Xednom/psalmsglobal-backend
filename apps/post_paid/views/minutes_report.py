from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters

from apps.authentication.models import Client
from apps.post_paid.models import MinutesReport
from apps.post_paid.serializers import MinutesReportSerializer

User = get_user_model()


__all__ = ("MinutesReportViewSet",)


class MinutesReportViewSet(viewsets.ModelViewSet):
    serializer_class = MinutesReportSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if current_user:
            qs = MinutesReport.objects.select_related("client").filter(client__user__in=user)
            return qs
        elif current_user.is_superuser:
            qs = MinutesReport.objects.all()
            return qs
