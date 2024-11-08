from django.urls import include, path
from rest_framework import routers

from apps.post_paid.views import (
    AccountBalanceViewSet,
    AccountChargeViewSet,
    InterestedToBuyViewSet,
    InterestedToSellViewSet,
    GeneralCallViewSet,
    CustomerInteractionPostPaidViewSet,
    CreateCustomerInteractionPostPaidComment,
    InteractionRecordViewSet,
    MinutesReportViewSet,
    MonthlyChargeViewSet,
    PostPaidViewSet,
    SubscriptionViewSet,
    JobOrderPostPaidViewSet,
    JobOrderViewSet,
    CreateJobOrderComment,
    PlanTypeListView,
    CostOfPlanListView,
    TicketSummaryViewSet,
    JobOrderTicketSummaryViewSet,
    TicketSummaryInteractionRecordViewSet,
    CreateJobOrderTicketSummaryComment,
    CreateTicketSummaryComment
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
    r"customer-interaction-post-paid",
    CustomerInteractionPostPaidViewSet,
    basename="customer-interaction-post-paid",
)
router.register(
    r"interaction-record", InteractionRecordViewSet, basename="interaction-record"
)
router.register(r"minutes-report", MinutesReportViewSet, basename="minutes-report")
router.register(r"monthly-charge", MonthlyChargeViewSet, basename="minutes-charge")
router.register(r"post-paid", PostPaidViewSet, basename="post-paid")
router.register(r"subscription", SubscriptionViewSet, basename="subscription-list")
router.register(
    r"job-order", JobOrderPostPaidViewSet, basename="job-order-interaction-list"
)
router.register(r"job-order-general", JobOrderViewSet, basename="job-order-list")
router.register(r"ticket-summary", TicketSummaryViewSet, basename="ticket-summary")
router.register(
    r"job-order-ticket-summary",
    JobOrderTicketSummaryViewSet,
    basename="job-order-ticket-summary",
)
router.register(
    r"ticket-summary-interaction",
    TicketSummaryInteractionRecordViewSet,
    basename="ticket-summary-interaction",
)

app_name = "post_paid"

urlpatterns = [
    path("post-paid/", include(router.urls)),
    path(
        "customer-interaction-post-paid/<int:id>/comment/",
        CreateCustomerInteractionPostPaidComment.as_view(),
        name="customer-interaction-post-paid-comment",
    ),
    path(
        "job-order/<int:id>/comment/",
        CreateJobOrderComment.as_view(),
        name="job-order-comment",
    ),
    path("post-paid/plan-types/", PlanTypeListView.as_view(), name="plan-type-list"),
    path(
        "post-paid/cost-of-plan/",
        CostOfPlanListView.as_view(),
        name="cost-of-plan-list",
    ),
    path(
        "job-order-ticket-summary/<int:id>/comment/",
        CreateJobOrderTicketSummaryComment.as_view(),
        name="job-order-ticket-summary-comment",
    ),
    path(
        "ticket-summary/<int:id>/comment/",
        CreateTicketSummaryComment.as_view(),
        name="ticket-summary-comment",
    ),
]
