from django.db import models
from import_export import resources
from apps.callme.models import Form


class FormResource(resources.ModelResource):
    class Meta:
        model = Form
        fields = (
            "form_title",
            "company__company_name",
            "customer_interaction_post_paid__ticket_number",
            "original_script",
        )
