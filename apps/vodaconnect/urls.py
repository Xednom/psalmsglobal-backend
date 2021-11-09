from django.urls import include, path
from rest_framework import routers

from apps.vodaconnect.views import (
    ActivePlanDetailViewSet,
    OtherChargeViewSet,
    PlanSummaryAndPaymentViewSet,
    VoipInformationViewSet,
    ActivationDetailViewSet,
    PlanDetailViewSet,
    SubscriberStatusViewSet,
    ForwardingInformationViewSet,
    VodaconnectSignUpViewSet
)

router = routers.DefaultRouter()

router.register(
    r"active-plan-detail", ActivePlanDetailViewSet, basename="active-plan-detail"
)
router.register(r"other-charge", OtherChargeViewSet, basename="other-charge")
router.register(
    r"plan-summary-and-payment",
    PlanSummaryAndPaymentViewSet,
    basename="plan-summary-and-payment",
)
router.register(
    r"voip-information", VoipInformationViewSet, basename="voip-information"
)
router.register(
    r"activation-detail", ActivationDetailViewSet, basename="activation-detail"
)
router.register(r"plan-detail", PlanDetailViewSet, basename="plan-detail")
router.register(
    r"subscriber-status", SubscriberStatusViewSet, basename="subscriber-status"
)
router.register(
    r"forwarding-information",
    ForwardingInformationViewSet,
    basename="forwarding-information",
)
router.register(
    r"vodaconnect-signup",
    VodaconnectSignUpViewSet,
    basename="vodaconnect-signup",
)

app_name = "vodaconnect"

urlpatterns = [path("vodaconnect/", include(router.urls))]
