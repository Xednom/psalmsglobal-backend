from apps.callme.models.company import Company
from django.urls import include, path
from rest_framework import routers

from apps.callme.views import (
    CompanyViewSet,
    CrmViewSet,
    PhoneSystemViewSet,
    VodaconnectPlanViewSet,
    VodaconnectLineTypeViewSet,
    FormViewSet,
    ScriptViewSet,
    StateViewSet,
    CountyViewSet,
    CallMeInfoViewSet,
    OfferStatusViewSet,
    PropertyInfoViewSet,
    FileUploadView,
    FormView
)

router = routers.DefaultRouter()

router.register(r"company", CompanyViewSet, basename="company")
router.register(r"crm", CrmViewSet, basename="crm")
router.register(r"phone-system", PhoneSystemViewSet, basename="phone-system")
router.register(r"vodaconnect-plan", VodaconnectPlanViewSet, basename="vodaconnect-plan")
router.register(r"vodaconnect-line-type", VodaconnectLineTypeViewSet, basename="vodaconnect-line-type")
router.register(r"script", ScriptViewSet, basename="script")
router.register(r"form", FormViewSet, basename="form")
router.register(r"state", StateViewSet, basename="state")
router.register(r"county", CountyViewSet, basename="county")
router.register(r"callme-info", CallMeInfoViewSet, basename="callme-info")
router.register(r"offer-status", OfferStatusViewSet, basename="offer-status")
router.register(r"property-info", PropertyInfoViewSet, basename="property-info")

app_name = "callme"

urlpatterns = [
    path("callme/", include(router.urls), name="callme"),
    path("file-upload/", FileUploadView.as_view(), name="file-upload"),
    path("interaction-form/<int:id>/", FormView.as_view(), name="form-view")
]