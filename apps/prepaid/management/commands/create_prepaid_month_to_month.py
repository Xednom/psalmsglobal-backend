import calendar
import datetime

from decimal import Decimal

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.prepaid.models import (
    AccountBalance,
    MinutesReport,
    CustomerInteractionPrepaid,
    InteractionRecord,
    JobOrderPrepaid,
    Prepaid,
    PaymentSummary,
)


class Command(BaseCommand):
    help = """Automatically create Month to Month for every user in the system.
        Note: for this to work, the Client should have a Plan Details
    """

    def handle(self, *args, **kwargs):

        today = datetime.datetime.now()
        month_year = str(calendar.month_abbr[today.month]) + "/" + str(today.year)

        client_name = (
            Prepaid.objects.all()
            .select_related("client", "plan_type")
            .values_list("client", flat=True)
            .distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            client_minutes = MinutesReport.objects.filter(client=i).exists()

            cust_interaction_overview = (
                InteractionRecord.objects.filter(client=i)
                .select_related(
                    "customer_interaction_prepaid",
                    "client",
                    "agent",
                )
                .aggregate(total_minutes=Sum("total_minutes"))
            )

            general_request_total_mins = (
                JobOrderPrepaid.objects.filter(client=i)
                .select_related("client", "caller_interaction_record")
                .aggregate(total_time_consumed=Sum("total_time_consumed"))
            )

            print(cust_interaction_overview["total_minutes"])
            print(general_request_total_mins["total_time_consumed"])

            if (
                cust_interaction_overview["total_minutes"] == 0
                and general_request_total_mins["total_time_consumed"] == None
            ):
                if client_minutes:
                    MinutesReport.objects.filter(
                        client=i, month_year=month_year
                    ).select_related("client").update(
                        client=i,
                        month_year=month_year,
                        customer_interaction_mins_overview=0,
                        general_request_mins_overview=0.00,
                        consumed_minutes=0.00,
                    )
                else:
                    MinutesReport.objects.create(
                        client=i,
                        month_year=month_year,
                        customer_interaction_mins_overview=0,
                        general_request_mins_overview=0.00,
                        consumed_minutes=0.00,
                    )
            else:
                if client_minutes:
                    MinutesReport.objects.filter(
                        client=i, month_year=month_year
                    ).select_related("client").update(
                        client=i,
                        month_year=month_year,
                        customer_interaction_mins_overview=cust_interaction_overview[
                            "total_minutes"
                        ],
                        general_request_mins_overview=general_request_total_mins[
                            "total_time_consumed"
                        ],
                        consumed_minutes=cust_interaction_overview["total_minutes"]
                        + general_request_total_mins["total_time_consumed"],
                    )
                else:
                    MinutesReport.objects.create(
                        client=i,
                        month_year=month_year,
                        customer_interaction_mins_overview=cust_interaction_overview[
                            "total_minutes"
                        ],
                        general_request_mins_overview=general_request_total_mins[
                            "total_time_consumed"
                        ],
                        consumed_minutes=cust_interaction_overview["total_minutes"]
                        + general_request_total_mins["total_time_consumed"],
                    )
