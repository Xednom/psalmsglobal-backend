from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.post_paid.models import AccountBalance, MinutesReport


class Command(BaseCommand):
    help = "Automatically create Account balance for every user in the system monthly."

    def handle(self, *args, **kwargs):
        client_name = (
            MinutesReport.objects.all().values_list("client", flat=True).distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            client_balance = AccountBalance.objects.filter(client=i).exists()
            client_total_minutes = MinutesReport.objects.filter(client=i).aggregate(
                total_minutes=Sum("plan_allocated_minutes")
            )
            client_total_spending = MinutesReport.objects.filter(client=i).aggregate(
                total_spending=Sum("cost_of_plan")
            )
            client_account_total_minutes = MinutesReport.objects.filter(
                client=i
            ).aggregate(total_monthly_usage=Sum("monthly_usage"))

            if (
                client_total_minutes["total_minutes"]
                and client_total_spending["total_spending"]
                and client_account_total_minutes["total_monthly_usage"]
            ):
                if client_balance:
                    AccountBalance.objects.filter(client=i).update(
                        account_total_aquired_minutes=client_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=client_total_spending["total_spending"],
                        account_total_mins_used=client_account_total_minutes[
                            "total_monthly_usage"
                        ],
                        account_total_mins_unused=client_total_minutes["total_minutes"]
                        - client_account_total_minutes["total_monthly_usage"],
                    )
                else:
                    AccountBalance.objects.create(
                        client=i,
                        account_total_aquired_minutes=client_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=client_total_spending["total_spending"],
                        account_total_mins_used=client_account_total_minutes[
                            "total_monthly_usage"
                        ],
                        account_total_mins_unused=client_total_minutes["total_minutes"]
                        - client_account_total_minutes["total_monthly_usage"],
                    )
