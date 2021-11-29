import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_company_view(client, auto_login_user):
    client = auto_login_user()
    url = reverse("callme:company-list")
    response = client.get(url)
    assert response.status_code == 200
