import xlrd
import os

from django.contrib.auth import get_user, get_user_model

from django_filters import CharFilter
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions

from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.callme.models import Company, PropertyInfo, OfferStatus, PropertyFileInfo
from apps.callme.serializers import (
    CallMeInfoSerializer,
    OfferStatusSerializer,
    PropertyFileSerializer,
)

User = get_user_model()


__all__ = (
    "CallMeInfoViewSet",
    "OfferStatusViewSet",
    "PropertyInfoViewSet",
    "FileUploadView",
)


class OfferStatusViewSet(viewsets.ModelViewSet):
    queryset = OfferStatus.objects.all()
    serializer_class = OfferStatusSerializer
    permission_classes = [permissions.IsAuthenticated]


class CallMeInfoFilter(filters.FilterSet):
    apn = CharFilter(field_name="apn", lookup_expr="icontains")
    reference = CharFilter(field_name="reference", lookup_expr="icontains")
    company_name = CharFilter(field_name="company_name", lookup_expr="icontains")

    class Meta:
        model = PropertyInfo
        fields = ("apn", "reference", "company_name")


class CallMeInfoViewSet(viewsets.ModelViewSet):
    queryset = PropertyInfo.objects.select_related("company").all()
    serializer_class = CallMeInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CallMeInfoFilter


class PropertyInfoViewSet(viewsets.ModelViewSet):
    serializer_class = CallMeInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        if (
            current_user.designation_category == "current_client"
            or current_user.designation_category == "new_client"
            or current_user.designation_category == "affiliate_partner"
        ):
            qs = PropertyInfo.objects.select_related("company", "offer_status").filter(
                company__client__user__in=user
            )
            return qs
        elif current_user.is_superuser:
            qs = PropertyInfo.objects.all()
            return qs


class FileUploadView(APIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = PropertyFileSerializer

    def post(self, request, format=None):
        file_obj = request.data["file"]

        if file_obj:
            loc = "{file_obj}".format(file_obj=file_obj)
            wb = xlrd.open_workbook(loc)
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)

            for i in range(sheet.nrows):
                if sheet.cell_value(i, 0):
                    company = sheet.cell_value(i, 0)
                    apn = sheet.cell_value(i, 1)
                    reference = sheet.cell_value(i, 2)
                    property_size = sheet.cell_value(i, 3)
                    short_legal_description = sheet.cell_value(i, 4)
                    property_address = sheet.cell_value(i, 5)
                    property_city = sheet.cell_value(i, 6)
                    property_county = sheet.cell_value(i, 7)
                    property_state = sheet.cell_value(i, 8)
                    property_zip = sheet.cell_value(i, 9)
                    address_modification = sheet.cell_value(i, 10)
                    first_name = sheet.cell_value(i, 12)
                    last_name = sheet.cell_value(i, 13)
                    company_name = sheet.cell_value(i, 14)
                    buyer_offer_amount = sheet.cell_value(i, 15)
                    buyer_approved_option_amount = sheet.cell_value(i, 16)
                    buyer_other_terms = sheet.cell_value(i, 17)
                    buyer_notes = sheet.cell_value(i, 18)
                    seller_offer_amount = sheet.cell_value(i, 19)
                    seller_other_offer_terms = sheet.cell_value(i, 20)
                    seller_notes = sheet.cell_value(i, 21)

                    co = Company.objects.filter(company_name=company).first()

                    property_info = PropertyInfo.objects.create(
                        company=co,
                        apn=apn,
                        reference=reference,
                        property_size=property_size,
                        short_legal_description=short_legal_description,
                        property_address=property_address,
                        property_city=property_city,
                        property_county=property_county,
                        property_state=property_state,
                        property_zip=property_zip,
                        full_name=first_name + " " + last_name,
                        company_name=company_name,
                        buyer_offer_amount=buyer_offer_amount,
                        approved_option_amount=buyer_approved_option_amount,
                        other_terms=buyer_other_terms,
                        seller_offer_amount=seller_offer_amount,
                        other_offer_terms=seller_other_offer_terms,
                        notes=seller_notes,
                    )
        return Response(status=201)
