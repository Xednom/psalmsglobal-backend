from django.db import models

from apps.core.models import TimeStamped


__all__ = ("AttributeType", "Form", "Script")


class AttributeType(TimeStamped):
    text = models.CharField(max_length=500, blank=True)
    question = models.TextField(blank=True)


class Form(TimeStamped):
    form_title = models.CharField(max_length=250)
    attribute = models.ForeignKey(
        AttributeType, related_name="form_attributes", on_delete=models.CASCADE
    )
    value_text = models.CharField(max_length=250, blank=True)
    value_question = models.TextField(blank=True)


class Script(TimeStamped):
    company = models.ForeignKey(
        "callme.Company", related_name="company_scripts", on_delete=models.CASCADE
    )
    company_address = models.CharField(max_length=250, blank=True)
    form = models.ForeignKey(
        Form, related_name="form_scripts", on_delete=models.CASCADE
    )
    mailing_lists = models.CharField(max_length=500)

    def get_company_address(self):
        return self.company.company_complete_address

    def save(self, *args, **kwargs):
        self.company_address = self.get_company_address()
        super(self, Script).save(*args, **kwargs)
