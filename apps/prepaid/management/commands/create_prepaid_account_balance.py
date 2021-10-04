from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.prepaid.models import (
    AccountBalance,
    MinutesReport,
    InteractionRecord,
    Prepaid,
    PaymentSummary,
)


class Command(BaseCommand):
    help = """Automatically create Account balance for every user in the system monthly.
        Note: for this to work, the Client should have a Plan Details
    """

    def handle(self, *args, **kwargs):
        client_name = (
            Prepaid.objects.all()
            .select_related("client", "plan_type")
            .values_list("client", flat=True)
            .distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            client_balance = AccountBalance.objects.filter(client=i).exists()

            account_total_minutes_used = (
                MinutesReport.objects.filter(client=i)
                .select_related("client")
                .aggregate(consumed_minutes=Sum("consumed_minutes"))
            )

            account_total_aquired_minutes = (
                PaymentSummary.objects.filter(client=i)
                .select_related("client")
                .aggregate(total_converted_minutes=Sum("total_converted_minutes"))
            )
            account_total_spending = (
                PaymentSummary.objects.filter(client=i)
                .select_related("client")
                .aggregate(total_amount_paid=Sum("total_amount_paid"))
            )
            account_total_mins_unused = (
                account_total_aquired_minutes["total_converted_minutes"]
                - account_total_minutes_used["consumed_minutes"]
            )

            if (
                account_total_mins_unused
                and account_total_spending["total_amount_paid"]
                and account_total_aquired_minutes["total_converted_minutes"]
            ):

                if client_balance:

                    AccountBalance.objects.filter(client=i).select_related(
                        "client"
                    ).update(
                        client=i,
                        account_total_aquired_minutes=account_total_aquired_minutes[
                            "total_converted_minutes"
                        ],
                        account_total_spending=account_total_spending[
                            "total_amount_paid"
                        ],
                        account_total_mins_used=account_total_minutes_used[
                            "consumed_minutes"
                        ],
                        account_total_mins_unused=account_total_mins_unused,
                    )
                else:
                    AccountBalance.objects.create(
                        client=i,
                        account_total_aquired_minutes=account_total_aquired_minutes[
                            "total_converted_minutes"
                        ],
                        account_total_spending=account_total_spending[
                            "total_amount_paid"
                        ],
                        account_total_mins_used=account_total_minutes_used[
                            "consumed_minutes"
                        ],
                        account_total_mins_unused=account_total_mins_unused,
                    )
