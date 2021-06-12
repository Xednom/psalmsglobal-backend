from django.db import models
from django.db.models.fields import CharField
from django_mysql.models import ListTextField
from apps.core.models import TimeStamped


__all__ = ("AttributeDataType", "Attribute", "Form", "Script")


class AttributeDataType(models.TextChoices):
    text = "text", ("Text")
    question = "question", ("Question")


class Form(TimeStamped):
    form_title = models.CharField(max_length=250)
    company = models.ForeignKey(
        "callme.Company",
        related_name="company_forms",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.form_title}"


class Attribute(TimeStamped):
    form = models.ForeignKey(
        Form, related_name="attribute_forms", on_delete=models.SET_NULL,
        blank=True, null=True
    )
    data_type = models.CharField(choices=AttributeDataType.choices, max_length=20)
    value_text = models.CharField(max_length=500, blank=True)
    value_question = models.TextField(blank=True)

    def __str__(self):
        return f"{self.form}"


class Script(TimeStamped):
    company = models.ForeignKey(
        "callme.Company", related_name="company_scripts", on_delete=models.CASCADE
    )
    company_address = models.CharField(max_length=250, blank=True)
    form = models.ForeignKey(
        Form, related_name="form_scripts", on_delete=models.CASCADE
    )
    mailing_lists = ListTextField(
        base_field=models.CharField(max_length=500),
        size=100
    )
    status = models.BooleanField(default=True)

    def get_company_address(self):
        if self.company:
            return self.company.company_complete_address
        else:
            return ""

    def save(self, *args, **kwargs):
        self.company_address = self.get_company_address()
        super(Script, self).save(*args, **kwargs)
