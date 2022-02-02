from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404, CreateAPIView

from apps.authentication.models import Client
from apps.post_paid.models import CustomerInteractionPostPaid
from apps.prepaid.models import CustomerInteractionPrepaid
from apps.grading.serializers import (
    PostpaidInteractionRateSerializer,
    PrepaidInteractionRateSerializer,
)


__all__ = ("PostpaidInteractionRatingView", "PrepaidInteractionRatingView")


class PostpaidInteractionRatingView(generics.CreateAPIView):
    serializer_class = PostpaidInteractionRateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        client = Client.objects.get(user=user)
        post_paid_id = self.kwargs.get("id")
        post_paid = get_object_or_404(CustomerInteractionPostPaid, id=post_paid_id)
        serializer.save(client=client, post_paid=post_paid)


class PrepaidInteractionRatingView(generics.CreateAPIView):
    serializer_class = PrepaidInteractionRateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        client = Client.objects.get(user=user)
        prepaid_id = self.kwargs.get("id")
        prepaid = get_object_or_404(CustomerInteractionPrepaid, id=prepaid_id)
        serializer.save(client=client, prepaid=prepaid)
