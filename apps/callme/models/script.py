from django.db import models

from apps.core.models import TimeStamped


class AttributeType(TimeStamped):
    text = "text", ("Text")
    question = "question", ("Question")


class Form(TimeStamped):
    form_title = models.CharField(max_length=250)
    attribute = models.ForeignKey(AttributeType, on_delete=models.CASCADE)
    value_text = models.CharField(max_length=250, blank=True)
    value_question = models.TextField(blank=True)


class Script(TimeStamped):
    company = models.ForeignKey("callme.Company", on_delete=models.CASCADE)
    company_address = models.CharField(max_length=250, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    mailing_lists = models.CharField(max_length=500)

    def get_company_address(self):
        return self.company.company_complete_address
    
    def save(self, *args, **kwargs):
        self.company_address = self.get_company_address()
        super(self, Script).save(*args, **kwargs)
