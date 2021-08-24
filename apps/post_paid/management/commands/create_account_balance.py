from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.post_paid.models import (
    AccountBalance,
    MinutesReport,
    PostPaid,
    MonthlyCharge,
    InteractionRecord,
    JobOrderPostPaid,
)


class Command(BaseCommand):
    help = """Automatically create Account balance for every user in the system monthly.
        Note: for this to work, the Client should have a Plan Details
    """

    def handle(self, *args, **kwargs):
        client_name = (
            PostPaid.objects.all()
            .select_related("client", "plan_type")
            .values_list("client", flat=True)
            .distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            client_balance = AccountBalance.objects.filter(client=i).exists()
            client_total_minutes = (
                PostPaid.objects.select_related("client", "plan_type")
                .filter(client=i, recurring_bill=True, account_status=True)
                .aggregate(total_minutes=Sum("total_minutes"))
            )
            used = (
                AccountBalance.objects.filter(client=i)
                .select_related("client")
                .aggregate(account_total_mins_used=Sum("account_total_mins_used"))
            )
            acquired = (
                AccountBalance.objects.filter(client=i)
                .select_related("client")
                .aggregate(total_acquired=Sum("account_total_aquired_minutes"))
            )

            monthly_used = (
                MinutesReport.objects.filter(client=i)
                .select_related("client")
                .aggregate(monthly_usage=Sum("monthly_usage"))
            )

            account_cost_of_plan = (
                MonthlyCharge.objects.filter(client=i)
                .select_related("client")
                .aggregate(cost_of_plan=Sum("cost_of_plan"))
            )

            account_total_minutes = (
                MonthlyCharge.objects.filter(client=i)
                .select_related("client")
                .aggregate(total_minutes=Sum("total_minutes"))
            )

            if (
                client_total_minutes["total_minutes"] == None
                and monthly_used["monthly_usage"] == None
                and used["account_total_mins_used"] == None
                or acquired["total_acquired"] == None
            ):

                if client_balance:

                    AccountBalance.objects.filter(client=i).select_related(
                        "client"
                    ).update(
                        client=i,
                        account_total_aquired_minutes=account_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=account_cost_of_plan["cost_of_plan"],
                        account_total_mins_used=monthly_used["monthly_usage"],
                        account_total_mins_unused=account_total_minutes["total_minutes"]
                        - monthly_used["monthly_usage"],
                    )
                else:
                    account_total_minutes = (
                        MonthlyCharge.objects.filter(client=i)
                        .select_related("client")
                        .aggregate(total_minutes=Sum("total_minutes"))
                    )
                    AccountBalance.objects.create(
                        client=i,
                        account_total_aquired_minutes=account_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=account_cost_of_plan["cost_of_plan"],
                        account_total_mins_used=monthly_used["monthly_usage"],
                        account_total_mins_unused=account_total_minutes["total_minutes"]
                        - monthly_used["monthly_usage"],
                    )
            else:
                if client_balance:
                    AccountBalance.objects.filter(client=i).select_related(
                        "client"
                    ).update(
                        client=i,
                        account_total_aquired_minutes=account_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=account_cost_of_plan["cost_of_plan"],
                        account_total_mins_used=monthly_used["monthly_usage"],
                        account_total_mins_unused=account_total_minutes["total_minutes"]
                        - monthly_used["monthly_usage"],
                    )
