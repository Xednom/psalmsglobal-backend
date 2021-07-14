from django.contrib.auth import get_user, get_user_model

from rest_framework import viewsets, permissions, filters, generics

from apps.authentication.models import Client
from apps.post_paid.models import PostPaid, PlanType, CostPlan
from apps.post_paid.serializers import (
    PostPaidSerializer,
    PlanTypeSerializer,
    CostPlanSerializer,
)

User = get_user_model()


__all__ = ("PostPaidViewSet", "PlanTypeListView", "CostOfPlanListView")


class PlanTypeListView(generics.ListAPIView):
    serializer_class = PlanTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PlanType.objects.all()


class CostOfPlanListView(generics.ListAPIView):
    serializer_class = CostPlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CostPlan.objects.all()


class PostPaidViewSet(viewsets.ModelViewSet):
    serializer_class = PostPaidSerializer
    permisson_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        clients = User.objects.filter(username=current_user)
        client = clients.all()
        if current_user:
            qs = PostPaid.objects.select_related(
                "client", "plan_type", "cost_of_plan"
            ).filter(client__user__in=client)
            return qs
        elif current_user.is_superuser:
            qs = PostPaid.objects.all()
            return qs
