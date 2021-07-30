from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.post_paid.models import (
    AccountBalance,
    MinutesReport,
    MonthlyCharge,
    InteractionRecord,
    JobOrderPostPaid,
)


class Command(BaseCommand):
    help = "Automatically create Account balance for every user in the system monthly."

    def handle(self, *args, **kwargs):
        client_name = (
            MonthlyCharge.objects.all()
            .select_related("client", "plan_type")
            .values_list("client", flat=True)
            .distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            client_balance = AccountBalance.objects.filter(client=i).exists()
            client_total_minutes = (
                MonthlyCharge.objects.select_related("client", "plan_type")
                .filter(client=i)
                .aggregate(total_minutes=Sum("total_minutes"))
            )
            client_total_spending = (
                MonthlyCharge.objects.filter(client=i)
                .select_related("client", "plan_type")
                .aggregate(total_spending=Sum("cost_of_plan"))
            )
            client_total_mins_used = (
                InteractionRecord.objects.filter(client=i)
                .select_related("customer_interaction_post_paid", "client", "agent")
                .aggregate(total_mins_used=Sum("total_minutes"))
            )
            client_jo_total_mins_used = (
                JobOrderPostPaid.objects.filter(client=i)
                .select_related("caller_interaction_record", "client")
                .prefetch_related("va_assigned")
                .aggregate(total_job_mins_used=Sum("total_time_consumed"))
            )

            account_mins_used = (
                client_total_mins_used["total_mins_used"]
                + client_jo_total_mins_used["total_job_mins_used"]
            )

            if client_total_minutes["total_minutes"] and account_mins_used:
                if client_balance:
                    AccountBalance.objects.filter(client=i).select_related(
                        "client"
                    ).update(
                        account_total_aquired_minutes=client_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=client_total_spending["total_spending"],
                        account_total_mins_used=account_mins_used,
                        account_total_mins_unused=client_total_minutes["total_minutes"]
                        - account_mins_used,
                    )
                else:
                    AccountBalance.objects.create(
                        client=i,
                        account_total_aquired_minutes=client_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=client_total_spending["total_spending"],
                        account_total_mins_used=account_mins_used,
                        account_total_mins_unused=client_total_minutes["total_minutes"]
                        - account_mins_used,
                    )
