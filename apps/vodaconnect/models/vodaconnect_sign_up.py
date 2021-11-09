from django.db import models

from apps.core.models import TimeStamped


__all__ = ("VodaconnectSignUp",)


class VodaconnectSignUp(TimeStamped):
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_vodaconnect_sign_up",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    file_description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f"{self.file_description} - {self.url}"
