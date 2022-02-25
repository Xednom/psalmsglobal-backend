from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, filters, generics
from djoser.email import ConfirmationEmail, PasswordResetEmail

from .models import Staff, Client
from .serializers import (
    StaffCodeSerializer,
    StaffSerializer,
    ClientSerializer,
    ClientCodeSerializer,
    UserAccountTypeSerializer,
)

User = get_user_model()


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    lookup_field = "user"
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Staff.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    lookup_field = "user"
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()


class ClientCodeViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["=client_code"]


class StaffCodeList(generics.ListAPIView):
    serializer_class = StaffCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Staff.objects.all()


class UserAccountTypeView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAccountTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class CallMeConfirmationEmail(ConfirmationEmail):
    template_name = "email/confirmation_email.html"


class CallMePasswordResetEmail(PasswordResetEmail):
    template_name = "email/forgot_password_email.html"
