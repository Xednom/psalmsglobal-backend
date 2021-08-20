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
                .filter(client=i)
                .aggregate(total_minutes=Sum("total_minutes"))
            )
            client_total_spending = (
                MonthlyCharge.objects.filter(client=i)
                .select_related("client", "plan_type")
                .aggregate(total_spending=Sum("cost_of_plan"))
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

            if (
                client_total_minutes["total_minutes"] == None
                and monthly_used["monthly_usage"] == None
                and used["account_total_mins_used"] == None
                or acquired["total_acquired"] == None
            ):

                if client_balance:
                    used = (
                        AccountBalance.objects.filter(client=i)
                        .select_related("client")
                        .aggregate(
                            account_total_mins_used=Sum("account_total_mins_used")
                        )
                    )
                    acquired = (
                        AccountBalance.objects.filter(client=i)
                        .select_related("client")
                        .aggregate(total_acquired=Sum("account_total_aquired_minutes"))
                    )
                    unused = Decimal(used["account_total_mins_used"]) - Decimal(
                        acquired["total_acquired"]
                    )

                    AccountBalance.objects.filter(client=i).select_related(
                        "client"
                    ).update(
                        account_total_aquired_minutes=client_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=client_total_spending["total_spending"],
                        account_total_mins_used=monthly_used["monthly_usage"],
                        account_total_mins_unused=unused,
                    )
                else:
                    if (
                        used["account_total_mins_used"] == None
                        and acquired["total_acquired"] == None
                    ):
                        AccountBalance.objects.create(
                            client=i,
                            account_total_aquired_minutes=client_total_minutes[
                                "total_minutes"
                            ],
                            account_total_spending=client_total_spending[
                                "total_spending"
                            ],
                            account_total_mins_used=monthly_used["monthly_usage"],
                            account_total_mins_unused=0.00,
                        )
                    else:
                        AccountBalance.objects.create(
                            client=i,
                            account_total_aquired_minutes=client_total_minutes[
                                "total_minutes"
                            ],
                            account_total_spending=client_total_spending[
                                "total_spending"
                            ],
                            account_total_mins_used=monthly_used["monthly_usage"],
                            account_total_mins_unused=unused,
                        )
            else:
                unused = Decimal(used["account_total_mins_used"]) - Decimal(
                    acquired["total_acquired"]
                )
                monthly_user = (
                    MinutesReport.objects.filter(client=i)
                    .select_related("client")
                    .aggregate(monthly_usage=Sum("monthly_usage"))
                )
                if client_balance:
                    AccountBalance.objects.filter(client=i).select_related(
                        "client"
                    ).update(
                        client=i,
                        account_total_aquired_minutes=client_total_minutes[
                            "total_minutes"
                        ],
                        account_total_spending=client_total_spending["total_spending"],
                        account_total_mins_used=monthly_user["monthly_usage"],
                        account_total_mins_unused=unused,
                    )
