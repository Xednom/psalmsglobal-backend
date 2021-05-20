from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import TimeStamped


class DesignationCategory(models.TextChoices):
    staff = "staff", ("Staff")
    new_client = "new_client", ("New Client")
    current_client = "current_client", ("Current Client")
    affiliate_partner = "affiliate_partner", ("Affiliate Partner")


class CompanyCategory(models.TextChoices):
    call_me = "call_me_ph", ("CallMe.Com.Ph")
    psalms_global = "psalms_global", ("PsalmsGlobal.Com")
    call_me_psalms_global = "call_me_ph", ("CallMe.Com.Ph/PsalmsGlobal.Com")


class User(AbstractUser):
    phone = models.CharField(blank=True, max_length=50)
    email = models.EmailField(unique=True)
    designation_category = models.CharField(
        choices=DesignationCategory.choices, blank=True, max_length=30
    )
    company_category = models.CharField(
        choices=CompanyCategory.choices, blank=True, max_length=40
    )
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone",
        "email",
        "designation_category",
        "company_category",
    ]

    @property
    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Client(TimeStamped):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    client_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_code = models.CharField(max_length=250, blank=True)
    affiliate_partner_name = models.CharField(max_length=250, blank=True)
    pin = models.CharField(max_length=5, blank=True)
    lead_information = models.TextField(
        blank=True, help_text="Where did you hear about our company?"
    )
    customer_id = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ["user__first_name"]

    def __str__(self):
        return self.user.user_full_name + " - " + self.client_code

    @property
    def client_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def create_client_code(self):
        initial_name = self.user.first_name + self.user.last_name
        client_code = ""

        for i in initial_name.upper().split():
            client_code += i[0]

        last_in = Client.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            client_code = client_code + "000" + str(int(seq) + 1)
            return client_code

        if self.id:
            client_code = client_code + "000" + str(self.id)
            return client_code

        in_id = last_in.id
        in_int = int(in_id)

        client_code = client_code + "000" + str(int(in_int) + 1)
        return client_code

    def create_customer_id(self):
        code = self.user.company_category
        customer_code = ""
        for i in code.upper().split():
            customer_code += i[0]
        last_in = Client.objects.all().order_by("id").last()
        if not last_in:
            for i in code.upper().split():
                customer_code += i[0]
            seq = 0
            customer_code = customer_code + "000" + str((int(seq) + 1))
            return customer_code

        if self.id:
            customer_code = customer_code + "000" + str(self.id)
            return customer_code

        in_id = last_in.id
        in_int = int(in_id)

        customer_code = customer_code + "000" + str(int(in_int) + 1)
        return customer_code

    def save(self, *args, **kwargs):
        self.client_code = self.create_client_code()
        self.customer_id = self.create_customer_id()
        super().save(*args, **kwargs)

    @property
    def client_name(self):
        return f"{self.user.user_full_name}"