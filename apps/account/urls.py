from apps.callme.models.company import Company
from django.urls import include, path
from rest_framework import routers

from apps.account.views import (
    LoginCredentialViewSet,
    AccountFileViewSet,
)

router = routers.DefaultRouter()

router.register(
    r"login-credentials", LoginCredentialViewSet, basename="login-credentials-list"
)
router.register(r"account-files", AccountFileViewSet, basename="account-files-list")

app_name = "account"
urlpatterns = [path("", include(router.urls))]
