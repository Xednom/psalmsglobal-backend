from django.db import models

from apps.core.models import TimeStamped


__all__ = ("County", "State")


class State(TimeStamped):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = "List of State in USA"
        verbose_name_plural = "List of States in USA"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class County(TimeStamped):
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "List of County in USA"
        verbose_name_plural = "List of Counties in USA"

    def __str__(self):
        return f"{self.name} - {self.state}"
