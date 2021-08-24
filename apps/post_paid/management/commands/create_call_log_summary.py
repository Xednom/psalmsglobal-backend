import calendar
import datetime

from decimal import Decimal
from datetime import date

from django.db.models import Sum, Q, Case, When, DecimalField
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.post_paid.models import (
    AccountBalance,
    MonthlyCharge,
    MinutesReport,
    InteractionRecord,
    JobOrderPostPaid,
    PostPaid,
    CustomerInteractionPostPaid,
)


class Command(BaseCommand):
    help = """Automatically create Call log summary/Minutes for every user in the system monthly.
        Note: this will only work if there is a Plan detail(Postpaid) for the Client.
        """

    def handle(self, *args, **kwargs):

        today = datetime.datetime.now()
        month_year = str(calendar.month_abbr[today.month]) + "/" + str(today.year)

        client_name = (
            PostPaid.objects.select_related("client")
            .filter(recurring_bill=True, account_status=True)
            .values_list("client", flat=True)
            .distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:

            client_minutes_report = PostPaid.objects.filter(
                client=i, recurring_bill=True, account_status=True
            ).exists()
            client_plan_detail_report = PostPaid.objects.filter(
                client=i, recurring_bill=True, account_status=True
            )
            client_minute_report = MinutesReport.objects.filter(
                client=i, month_year=month_year
            ).exists()

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
            if client_minutes_report:
                client_post_paid = PostPaid.objects.select_related(
                    "client", "plan_type"
                ).filter(client=i, recurring_bill=True, account_status=True)
                for post_paid in client_post_paid:
                    if post_paid:
                        minute_report_data = MinutesReport.objects.filter(client=i)
                        for item in minute_report_data:
                            if (
                                item.month_year == month_year
                                or client_total_mins_used["total_mins_used"] == None
                                and client_jo_total_mins_used["total_job_mins_used"]
                                == None
                            ):
                                MinutesReport.objects.filter(
                                    client=i, month_year=month_year
                                ).update(
                                    month_year=item.month_year,
                                    total_minutes_unused=item.plan_allocated_minutes
                                    - item.monthly_usage,
                                    plan_allocated_minutes=item.plan_allocated_minutes,
                                    ci_minutes_overview=client_total_mins_used[
                                        "total_mins_used"
                                    ],
                                    general_request_total_minutes=client_jo_total_mins_used[
                                        "total_job_mins_used"
                                    ],
                                    monthly_usage=Decimal(item.ci_minutes_overview)
                                    + Decimal(item.general_request_total_minutes),
                                    cost_of_plan=post_paid.cost_of_plan,
                                )

                        if client_minute_report:
                            minute_report_data = MinutesReport.objects.filter(client=i)
                            for item in minute_report_data:
                                if (
                                    client_total_mins_used["total_mins_used"] != None
                                    and client_jo_total_mins_used["total_job_mins_used"]
                                    != None
                                ):
                                    MinutesReport.objects.filter(
                                        client=i, month_year=month_year
                                    ).update(
                                        month_year=item.month_year,
                                        plan_allocated_minutes=item.plan_allocated_minutes,
                                        ci_minutes_overview=client_total_mins_used[
                                            "total_mins_used"
                                        ],
                                        general_request_total_minutes=client_jo_total_mins_used[
                                            "total_job_mins_used"
                                        ],
                                        monthly_usage=Decimal(item.ci_minutes_overview)
                                        + Decimal(item.general_request_total_minutes),
                                        total_minutes_unused=item.plan_allocated_minutes
                                        - item.monthly_usage,
                                        cost_of_plan=post_paid.cost_of_plan,
                                    )
                                elif (
                                    item
                                    and client_total_mins_used["total_mins_used"]
                                    == None
                                    and client_jo_total_mins_used["total_job_mins_used"]
                                    == None
                                ):
                                    MinutesReport.objects.filter(
                                        client=i, month_year=month_year
                                    ).update(
                                        month_year=item.month_year,
                                        plan_allocated_minutes=item.plan_allocated_minutes,
                                        ci_minutes_overview=0.00,
                                        general_request_total_minutes=0.00,
                                        monthly_usage=Decimal(item.ci_minutes_overview)
                                        + Decimal(item.general_request_total_minutes),
                                        cost_of_plan=post_paid.cost_of_plan,
                                        total_minutes_unused=item.plan_allocated_minutes
                                        - item.monthly_usage,
                                    )
                        elif (
                            client_total_mins_used["total_mins_used"] == None
                            and client_jo_total_mins_used["total_job_mins_used"] == None
                        ):
                            MinutesReport.objects.create(
                                client=i,
                                plan_type=post_paid.plan_type,
                                month_year=month_year,
                                total_minutes_unused=0.00,
                                plan_allocated_minutes=post_paid.total_minutes,
                                ci_minutes_overview=0.00,
                                general_request_total_minutes=0.00,
                                monthly_usage=0.00,
                                cost_of_plan=post_paid.cost_of_plan,
                            )
                        elif (
                            client_total_mins_used["total_mins_used"] != None
                            and client_jo_total_mins_used["total_job_mins_used"] != None
                        ):
                            MinutesReport.objects.create(
                                client=i,
                                plan_type=post_paid.plan_type,
                                month_year=month_year,
                                plan_allocated_minutes=post_paid.total_minutes,
                                ci_minutes_overview=client_total_mins_used[
                                    "total_mins_used"
                                ],
                                general_request_total_minutes=client_jo_total_mins_used[
                                    "total_job_mins_used"
                                ],
                                cost_of_plan=post_paid.cost_of_plan,
                            )
