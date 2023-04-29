from django.core.management.base import BaseCommand

from apps.authentication.models import Staff
from apps.post_paid.models import CustomerInteractionPostPaid, TicketSummary


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        interactions = CustomerInteractionPostPaid.objects.all()

        if interactions:
            for interaction in interactions:
                interaction_exists = TicketSummary.objects.filter(
                    ticket_number=interaction.ticket_number
                ).exists()

                if not interaction_exists:
                    TicketSummary.objects.get_or_create(
                        ticket_number=interaction.ticket_number,
                        company=interaction.company,
                        agent=interaction.agent,
                        apn=interaction.apn,
                        reference_number=interaction.reference_number,
                        county=interaction.county,
                        state=interaction.state,
                        address=interaction.address,
                        caller_full_name=interaction.caller_full_name,
                        caller_phone=interaction.caller_phone,
                        email=interaction.email,
                        reason_of_the_call=interaction.reason_of_the_call,
                        interested_to_sell=interaction.interested_to_sell,
                        interested_to_buy=interaction.interested_to_buy,
                        general_call=interaction.general_call,
                        crm=interaction.crm,
                        leads_transferred_crm=interaction.leads_transferred_crm,
                        internal_auditor=interaction.internal_auditor,
                    )
            print("All Customer interaction PostPaid are now in Ticket Summary")
