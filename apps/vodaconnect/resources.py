from import_export import resources

from apps.vodaconnect import models


class ActivePlanDetailResource(resources.ModelResource):
    class Meta:
        model = models.ActivePlanDetail
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "plan_type__name",
            "total_minutes_included",
            "cost_of_plan",
            "start_of_plan",
            "end_of_plan",
            "account_status",
            "recurring_bill",
        )


class ActivationDetailResource(resources.ModelResource):
    class Meta:
        model = models.ActivationDetail
        fields = (
            "client",
            "order_request_date",
            "request_date_initiated",
            "date_line_activated",
            "date_line_terminated",
            "phone_line_status",
            "client_company_user_category",
        )


class ForwardingInformationResource(resources.ModelResource):
    class Meta:
        model = models.ForwardingInformation
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "forwarding_number",
            "notes",
        )


class OtherChargeResource(resources.ModelResource):
    class Meta:
        model = models.OtherCharge
        fields = (
            "date",
            "client__user__first_name",
            "client__user__last_name",
            "vodaconnect_number",
            "type_charge",
            "amount",
            "payment_reference",
            "payment_status",
            "notes",
        )


class PlanDetailResource(resources.ModelResource):
    class Meta:
        model = models.PlanDetail
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "plan_type",
            "total_cost",
            "recurring_bill",
            "paypal_details_for_billing",
            "due_date",
        )


class PlanSummaryAndPaymentResource(resources.ModelResource):
    class Meta:
        model = models.PlanSummaryAndPayment
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "month_year",
            "plan_type",
            "total_minutes",
            "cost_of_plan",
            "payment_reference",
            "status",
            "date_of_paid",
        )


class PlanTypeResource(resources.ModelResource):
    class Meta:
        model = models.PlanType
        fields = ("name",)


class SubscriberStatusResource(resources.ModelResource):
    class Meta:
        model = models.SubscriberStatus
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "status_in_production",
            "type_of_request",
            "testimony",
        )


class VodaconnectSignUpResource(resources.ModelResource):
    class Meta:
        model = models.VodaconnectSignUp
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "file_description",
            "url",
        )


class VoipInformationResource(resources.ModelResource):
    class Meta:
        model = models.VoipInformation
        fields = (
            "client__user__first_name",
            "client__user__last_name",
            "vodaconnect_number",
            "client",
            "client_code",
            "company_name",
        )
