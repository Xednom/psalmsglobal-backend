from django.urls import include, path
from rest_framework import routers

from apps.prepaid.views import (
    AccountBalanceViewSet,
    AccountChargeViewSet,
    InterestedToBuyViewSet,
    InterestedToSellViewSet,
    GeneralCallViewSet,
    CustomerInteractionPrepaidViewSet,
    CreateCustomerInteractionPrepaidComment,
    MinutesReportViewSet,
    PrepaidPaymentSummaryViewSet,
    SubscriptionInfoViewSet,
    PrepaidSubscriptionViewSet,
    PrepaidViewSet,
    JobOrderPrepaidViewSet,
    JobOrderViewSet,
    InteractionRecordViewSet,
    CreateJobOrderComment,
)

router = routers.DefaultRouter()

router.register(r"account-balance", AccountBalanceViewSet, basename="account-balance")
router.register(r"account-charge", AccountChargeViewSet, basename="account-charge")
router.register(
    r"interested-to-buy", InterestedToBuyViewSet, basename="interested-to-buy"
)
router.register(
    r"interested-to-sell", InterestedToSellViewSet, basename="interested-to-sell"
)
router.register(r"general-call", GeneralCallViewSet, basename="general-call")
router.register(
    r"customer-interaction",
    CustomerInteractionPrepaidViewSet,
    basename="customer-interaction",
)
router.register(
    r"payment-summary", PrepaidPaymentSummaryViewSet, basename="prepaid-payment-summary"
)
router.register(
    r"subscription-info", SubscriptionInfoViewSet, basename="subscription-info"
)
router.register(
    r"prepaid-subscription", PrepaidSubscriptionViewSet, basename="prepaid-subscription"
)
router.register(r"minutes-report", MinutesReportViewSet, basename="minutes-report")
router.register(r"prepaid-account", PrepaidViewSet, basename="prepaid-account")
router.register(
    r"job-order", JobOrderPrepaidViewSet, basename="job-order-interaction-list"
)
router.register(r"job-order-general", JobOrderViewSet, basename="job-order-list")
router.register(
    r"interaction-record", InteractionRecordViewSet, basename="interaction-list"
)

app_name = "prepaid"

urlpatterns = [
    path("prepaid/", include(router.urls)),
    path(
        "customer-interaction-prepaid/<int:id>/comment/",
        CreateCustomerInteractionPrepaidComment.as_view(),
        name="customer-interaction-prepaid-comment",
    ),
    path(
        "prepaid/job-order/<int:id>/comment/",
        CreateJobOrderComment.as_view(),
        name="job-order-comment",
    ),
]
