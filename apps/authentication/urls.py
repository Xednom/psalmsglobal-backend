from rest_framework import routers

from django.urls import include, path

from .views import (
    StaffViewSet,
    ClientViewSet,
    ClientCodeViewSet,
    UserAccountTypeView,
    StaffCodeList,
)

router = routers.DefaultRouter()
router.register(r"staff", StaffViewSet, basename="staff")
router.register(r"client", ClientViewSet, basename="client")
router.register(r"client-code", ClientCodeViewSet, basename="client-code")


app_name = "auth"
urlpatterns = [
    path("", include(router.urls)),
    path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    path(
        "user-account-type/<int:id>/",
        UserAccountTypeView.as_view(),
        name="user-account-type",
    ),
    path("staff-code/", StaffCodeList.as_view(), name="staff-code"),
]
