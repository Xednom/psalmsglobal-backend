import calendar
import datetime

from decimal import Decimal

from django.db.models import F
from django.core.management.base import BaseCommand

from post_office.models import EmailTemplate
from post_office import mail

from apps.authentication.models import Client
from apps.prepaid.models import (
    InteractionRecord,
    JobOrderPrepaid,
    Prepaid,
    PrepaidSubscription,
    PlanType,
)


class Command(BaseCommand):
    help = """Automatically create Monthly subscription for every user in the system.
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
        if client:
            for i in client:
                client_monthly_subs = PrepaidSubscription.objects.filter(
                    client=i
                ).exists()

                client_monthly_fees = Prepaid.objects.filter(client=i).select_related(
                    "client", "subscription_type"
                )

                for item in client_monthly_fees:
                    if client_monthly_subs:
                        PrepaidSubscription.objects.filter(
                            client=i, month_year=month_year
                        ).update(
                            plan_type=item.subscription_type,
                            monthly_fee=item.monthly_fees,
                        )
                    elif today.strftime("%d") == "1":
                        PrepaidSubscription.objects.create(
                            client=item.client,
                            month_year=month_year,
                            plan_type=item.subscription_type,
                            monthly_fee=item.monthly_fees,
                            payment_status=False,
                        )
