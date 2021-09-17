from django.urls import include, path
from rest_framework import routers

from apps.newsfeed.models import NewsFeed, NewsFeedComment, newsfeed
from apps.newsfeed.views import NewsFeedViewSet, CreateNewsFeedComment

router = routers.DefaultRouter()

router.register(r"newsfeed", NewsFeedViewSet, basename="news-feed-list")

app_name = "newsfeed"

urlpatterns = [
    path("", include(router.urls)),
    path(
        "newsfeed/<int:id>/comment/",
        CreateNewsFeedComment.as_view(),
        name="newsfeed-comment",
    ),
]
