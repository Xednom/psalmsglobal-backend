from django.db import models

from apps.core.models import TimeStamped


__all__ = ("AccountCharge",)


class AccountCharge(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_account_charges",
        on_delete=models.DO_NOTHING,
    )
    agent = models.ForeignKey(
        "authentication.Staff",
        related_name="agent_account_charges",
        on_delete=models.DO_NOTHING,
    )
    ticket_number = models.CharField(max_length=250)
    date_called = models.DateField()
    total_minutes = models.DecimalField(max_digits=19, decimal_places=2)
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} - {self.ticket_number}"
