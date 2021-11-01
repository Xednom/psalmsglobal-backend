from django.db import models

from djmoney.models.fields import MoneyField

from apps.core.models import TimeStamped


__all__ = ("OtherCharge",)


class PaymentStatus(models.TextChoices):
    paid = "paid", ("Paid")
    unpaid = "unpaid", ("Unpaid")


class OtherCharge(TimeStamped):
    date = models.DateField()
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_other_charges",
        on_delete=models.CASCADE,
    )
    vodaconnect_number = models.CharField(max_length=250)
    type_charge = models.TextField()
    amount = MoneyField(
        max_digits=19,
        decimal_places=2,
        default_currency="USD",
        default=0.00,
        blank=True,
        null=True,
    )
    payment_reference = models.TextField(blank=True)
    payment_status = models.CharField(max_length=50, choices=PaymentStatus.choices)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client} vodaconnect number - {self.vodaconnect_number} with a type of charge {self.type_charge}"
