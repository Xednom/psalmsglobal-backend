import pytest

from django.urls import reverse


# @pytest.mark.django_db
# def test_company_list(client, auto_login_user):
#     client, user = auto_login_user()
#     url = reverse("callme:company-list")
#     response = client.get(url)
#     assert response.status_code == 200

@pytest.mark.django_db
def test_company_view(client, create_user, test_password):
    user = create_user()
    url = reverse("callme:company-list")
    client.login(username=user.username, password=test_password)
    response = client.get(url)
    assert response.status_code == 200
