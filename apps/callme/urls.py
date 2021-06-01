from apps.callme.models.company import Company
from django.urls import include, path
from rest_framework import routers

from apps.callme.views import (
    CompanyViewSet,
    CrmViewSet,
    PhoneSystemViewSet,
    AttributeTypeViewSet,
    FormViewSet,
    ScriptViewSet
)

router = routers.DefaultRouter()

router.register(r"company", CompanyViewSet, basename="company-list")
router.register(r"crm", CrmViewSet, basename="crm-list")
router.register(r"phone-system", PhoneSystemViewSet, basename="phone-system-list")
router.register(r"script", ScriptViewSet, basename="script-list")

app_name = "callme"

urlpatterns = [
    path("", include(router.urls))
]