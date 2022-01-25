from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Resolution", "ResolutionConversation")


class StatusChoices(models.TextChoices):
    pending = "pending", ("Pending")
    in_progress = "in_progress", ("In progress")
    on_hold = "on_hold", ("On hold")
    closed = "closed", ("Closed")
    resolution_provided = "resolution_provided", ("Resolution provided")


class Resolution(TimeStamped):
    category = models.ForeignKey(
        "core.ResolutionCategory",
        related_name="resolution_categories",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    description = models.TextField()
    assigned_to = models.ForeignKey(
        "authentication.Staff",
        related_name="staff_assigned_resolutions",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    client = models.ForeignKey(
        "authentication.Client",
        related_name="client_resolutions",
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=250, choices=StatusChoices.choices, default=StatusChoices.pending
    )

    class Meta:
        verbose_name = "Resolution"
        verbose_name_plural = "Resolutions"
        ordering = ["-created_at"]


class ResolutionConversation(TimeStamped):
    resolution = models.ForeignKey(
        Resolution, related_name="resolution_conversations", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "authentication.Staff",
        related_name="user_resolution_conversations",
        on_delete=models.CASCADE,
    )
    comment = models.TextField()
