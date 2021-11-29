import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("test", "test@example.com", "stronk-password")
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_detail(client, auto_login_user):
    client, user = auto_login_user()
    url = reverse("auth:user-me")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_auth(client, auto_login_user):
    client, user = auto_login_user()
    url = reverse("auth:user-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_list_unauth(client):
    url = reverse("auth:user-list")
    response = client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_user_detail_unauth(client):
    url = reverse("auth:user-me")
    response = client.get(url)
    assert response.status_code == 401