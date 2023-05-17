from post_office import mail

from django.db import models
from django.db.models.fields import CharField
from django_mysql.models import ListTextField
from apps.core.models import TimeStamped

from ckeditor.fields import RichTextField
from django_bleach.models import BleachField


__all__ = ("AttributeDataType", "Attribute", "Form", "Script")


class AttributeDataType(models.TextChoices):
    text = "text", ("Text")
    question = "question", ("Question")


class Form(TimeStamped):
    form_title = models.CharField(max_length=250, blank=True)
    company = models.ForeignKey(
        "callme.Company",
        related_name="company_forms",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    customer_interaction_post_paid = models.ForeignKey(
        "post_paid.CustomerInteractionPostPaid",
        related_name="customer_interaction_post_paid_forms",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    customer_interaction_prepaid = models.ForeignKey(
        "prepaid.CustomerInteractionPrepaid",
        related_name="customer_interaction_prepaid_forms",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    ticket_summary = models.ForeignKey(
        "post_paid.TicketSummary",
        related_name="ticket_summary_forms",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    mailing_lists = ListTextField(
        base_field=models.CharField(max_length=500), size=100, blank=True, null=True
    )
    mailing_lists_unpacked = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    original_script = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "List of Scripts per Company"

    def __str__(self):
        return f"{self.form_title}"

    def unpack_mailing_lists(self):
        mailing = []
        if self.mailing_lists:
            mailing = " ".join(self.mailing_lists)
        return mailing

    # @property
    # def get_mailing_list(self):
    #     if self.mailing_lists:
    #         mailing_lists = ", ".join(self.mailing_lists)
    #         return mailing_lists

    def save(self, *args, **kwargs):
        self.mailing_lists_unpacked = self.unpack_mailing_lists()
        super(Form, self).save(*args, **kwargs)


class Attribute(TimeStamped):
    form = models.ForeignKey(
        Form,
        related_name="attribute_forms",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    data_type = models.CharField(choices=AttributeDataType.choices, max_length=20)
    value_text = BleachField(blank=True)
    value_question = BleachField(blank=True)
    input_question = models.TextField(blank=True)

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
    mailing_lists = ListTextField(base_field=models.CharField(max_length=500), size=100)
    status = models.BooleanField(default=True)

    def get_company_address(self):
        if self.company:
            return self.company.company_complete_address
        else:
            return ""

    def save(self, *args, **kwargs):
        self.company_address = self.get_company_address()
        super(Script, self).save(*args, **kwargs)
