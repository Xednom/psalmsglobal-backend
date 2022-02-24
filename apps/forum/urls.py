from django.urls import include, path

from rest_framework import routers

from apps.forum.views import ThreadViewSet, CommentView, ReplyView


router = routers.DefaultRouter()

router.register(r"thread", ThreadViewSet, basename="thread")

app_name = "forum"
urlpatterns = [
    path("", include(router.urls)),
    path("thread/<int:id>/comment/", CommentView.as_view(), name="thread-comment"),
    path("reply/<int:id>/", ReplyView.as_view(), name="thread-reply"),
]
