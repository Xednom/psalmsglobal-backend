from rest_framework import serializers

from apps.post_paid.models import JobOrderPostPaid, CustomerInteractionPostPaid
from apps.authentication.models import Client, Staff


__all__ = ("JobOrderPostPaidSerializer",)


class JobOrderPostPaidSerializer(serializers.ModelSerializer):
    caller_interaction_record = serializers.SlugRelatedField(
        slug_field="ticket_number",
        queryset=CustomerInteractionPostPaid.objects.all(),
        allow_null=True,
        required=False,
    )

    class Meta:
        model = JobOrderPostPaid
        fields = (
            "id",
            "caller_interaction_record",
            "client",
            "client_file",
            "client_email",
            "va_assigned",
            "staff_email",
            "ticket_number",
            "request_date",
            "due_date",
            "job_title",
            "job_description",
            "client_notes",
            "va_notes",
            "management_notes",
            "status",
            "date_completed",
            "total_time_consumed",
            "url_of_the_completed_jo",
        )