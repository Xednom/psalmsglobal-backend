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
    PropertyInfoViewSet
)

router = routers.DefaultRouter()

router.register(r"company", CompanyViewSet, basename="company-list")
router.register(r"crm", CrmViewSet, basename="crm-list")
router.register(r"phone-system", PhoneSystemViewSet, basename="phone-system-list")
router.register(r"vodaconnect-plan", VodaconnectPlanViewSet, basename="vodaconnect-plan")
router.register(r"vodaconnect-line-type", VodaconnectLineTypeViewSet, basename="vodaconnect-line-type")
router.register(r"script", ScriptViewSet, basename="script-list")
router.register(r"form", FormViewSet, basename="form-list")
router.register(r"state", StateViewSet, basename="state-list")
router.register(r"county", CountyViewSet, basename="county-list")
router.register(r"callme-info", CallMeInfoViewSet, basename="callme-info-list")
router.register(r"offer-status", OfferStatusViewSet, basename="offer-status-list")
router.register(r"property-info", PropertyInfoViewSet, basename="property-info-list")

app_name = "callme"

urlpatterns = [
    path("", include(router.urls))
]