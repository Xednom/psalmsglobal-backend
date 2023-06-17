from django.db import models


class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ResolutionCategory(TimeStamped):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Resolution Category"
        verbose_name_plural = "Resolution Categories"


class Tagging(TimeStamped):
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)


class Comment(TimeStamped):
    user = models.ForeignKey(
        "authentication.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    comment = models.TextField()

    class Meta:
        abstract = True
