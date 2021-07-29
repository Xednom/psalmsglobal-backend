import calendar
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
    InteractionRecord,
    JobOrderPostPaid,
    PostPaid,
)


class Command(BaseCommand):
    help = "Automatically create Plan Summary and Payment for every user in the system monthly."

    def handle(self, *args, **kwargs):

        today = date.today()
        month_year = str(calendar.month_abbr[today.month]) + "/" + str(today.year)

        print(month_year)

        client_name = (
            MonthlyCharge.objects.all().values_list("client", flat=True).distinct()
        )
        client = Client.objects.filter(id__in=client_name)

        for i in client:
            client_monthly_charge = MonthlyCharge.objects.filter(client=i).exists()
            client_post_paid = PostPaid.objects.filter(client=i)
            for post_paid in client_post_paid:
                if post_paid.cost_of_plan:

                    MonthlyCharge.objects.create(
                        client=i,
                        month_year=month_year,
                        plan_type=post_paid.plan_type,
                        total_minutes=post_paid.total_minutes,
                        cost_of_plan=post_paid.cost_of_plan,
                    )