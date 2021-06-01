from django.urls import include, path
from rest_framework import routers

from apps.post_paid.views import SubscriptionViewSet

router = routers.DefaultRouter()

router.register(r"subscription", SubscriptionViewSet, basename="subscription-list")

app_name = "post_paid"

urlpatterns = [
    path("", include(router.urls))
]