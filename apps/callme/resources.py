from django.db import models
from import_export import resources
from apps.callme.models import (
    Form,
    PropertyInfo,
    State,
    County,
    Company,
    Crm,
    VodaconnectPlan,
    VodaconnectLineType,
    PhoneSystem,
)


class FormResource(resources.ModelResource):
    class Meta:
        model = Form
        fields = (
            "form_title",
            "company__company_name",
            "customer_interaction_post_paid__ticket_number",
            "original_script",
        )


class PropertyInfoResource(resources.ModelResource):
    class Meta:
        model = PropertyInfo
        fields = (
            "company"
            "apn"
            "reference"
            "property_size"
            "short_legal_description"
            "property_address"
            "property_city"
            "property_county"
            "property_state"
            "property_zip"
            "full_name"
            "company_name"
            "buyer_offer_amount"
            "approved_option_amount"
            "other_terms"
            "seller_offer_amount"
            "other_offer_terms"
            "notes"
            "offer_status__name"
        )


class StateResource(resources.ModelResource):
    class Meta:
        model = State
        fields = ("name",)


class CountyResource(resources.ModelResource):
    class Meta:
        model = County
        fields = (
            "name",
            "state__name",
        )


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "company_owner_name",
            "company_name",
            "business_type",
            "company_phone",
            "company_email",
            "company_complete_address",
            "company_forwarding_email",
            "paypal_email",
            "notes",
        )


class CrmResource(resources.ModelResource):
    class Meta:
        model = Crm
        fields = (
            "company__company_name",
            "crm" "type_of_crm" "crm_url" "crm_login" "notes",
        )


class VodaconnectPlanResource(resources.ModelResource):
    class Meta:
        model = VodaconnectPlan
        fields = ("range",)


class VodaconnectLineTypeResource(resources.ModelResource):
    class Meta:
        model = VodaconnectLineType
        fields = ("line",)


class PhoneSystemResource(resources.ModelResource):
    class Meta:
        model = PhoneSystem
        fields = (
            "company__company_name"
            "sub_number"
            "caller_id_detail"
            "vodaconnect_plan__range"
            "original_line"
            "call_forwarding_number"
            "vodaconnect_line_type__line"
        )
