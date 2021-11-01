from django.db import models

from apps.core.models import TimeStamped


__all__ = ("VodaconnectSignUp",)


class VodaconnectSignUp(TimeStamped):
    file_description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f"{self.file_description} - {self.url}"
