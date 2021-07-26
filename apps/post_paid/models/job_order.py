from django.contrib.auth import get_user, get_user_model

from django.db import models

from apps.core.models import TimeStamped
from apps.account.models import AccountFile

User = get_user_model()


__all__ = ("JobOrderPostPaid", "JobOrderComment")


class JobOrderStatus(models.TextChoices):
    na = "na", ("N/A")
    job_order_request = "job_order_request", ("Job order request")
    va_processing = "va_processing", ("VA Processing")
    management_processing = "management_processing", ("Management Processing")
    verified_job_order = "verified_job_order", ("Verified Job Order")
    on_hold = "on_hold", ("On Hold")
    canceled = "canceled", ("Canceled")
    follow_up = "follow_up", ("Follow up")
    dispute = "dispute", ("Dispute")
    complete = "complete", ("Complete")
    under_quality_review = "under_quality_review", ("Under Quality Review")
    daily_tasks = "daily_tasks", ("Daily Tasks")
    weekly_tasks = "weekly_tasks", ("Weekly Tasks")
    monthly_tasks = "monthly_tasks", ("Monthly Tasks")
    redo = "redo", ("Redo")
    pending = "pending", ("Pending")
    request_for_posting = "request_for_posting", ("Request for Posting")
    mark_as_sold_request = "mark_as_sold_request", ("Mark as Sold Request")
    initial_dd_processing = "initial_dd_processing", ("Initial DD Processing")
    initial_dd_complete = "initial_dd_complete", ("Initial DD Complete")
    dd_call_out_processing = "dd_call_out_processing", ("DD Call Out Processing")
    dd_call_out_complete = "dd_call_out_complete", ("DD Call Out Complete")
    duplicate_request = "duplicate_request", ("Duplicate Request")


class JobOrderPostPaid(TimeStamped):
    caller_interaction_record = models.ForeignKey(
        "post_paid.CustomerInteractionPostPaid",
        related_name="interaction_job_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    client = models.ForeignKey(
        "authentication.Client",
        related_name="clients_job_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    client_file = models.CharField(max_length=500, blank=True)
    client_email = models.EmailField(blank=True)
    va_assigned = models.ManyToManyField(
        "authentication.Staff", related_name="vas_job_orders", blank=True
    )
    staff_email = models.CharField(max_length=500, blank=True)
    ticket_number = models.CharField(max_length=100, blank=True)
    request_date = models.DateField()
    due_date = models.DateField()
    job_title = models.CharField(max_length=250)
    job_description = models.TextField()
    client_notes = models.TextField(blank=True)
    va_notes = models.TextField(blank=True)
    management_notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=100,
        choices=JobOrderStatus.choices,
        default=JobOrderStatus.na,
        blank=True,
    )
    date_completed = models.DateField(blank=True, null=True)
    total_time_consumed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    url_of_the_completed_jo = models.TextField(blank=True)

    class Meta:
        ordering = ["-ticket_number"]

    def __str__(self):
        return "Job Order general of " + str(self.ticket_number)

    def create_ticket_number(self):
        ticket_code = ""
        last_in = JobOrderPostPaid.objects.all().order_by("id").last()

        if not last_in:
            seq = 0
            ticket_number = "CMJ000" + str((int(seq) + 1))
            return ticket_number

        if self.id:
            if self.id >= 100:
                ticket_number = "CMJ" + str(self.id)
            elif self.id <= 9:
                ticket_number = "CMJ00" + str(self.id)
            elif self.id >= 10:
                ticket_number = "CMJ0" + str(self.id)
            return ticket_number

        in_id = last_in.id
        in_int = int(in_id)
        if in_int >= 100:
            ticket_code = "CMJ" + str(int(in_int) + 1)
        elif in_int < 10:
            ticket_code = "CMJ00" + str(int(in_int) + 1)
        elif in_int >= 10:
            ticket_code = "CMJ0" + str(int(in_int) + 1)

        return ticket_code

    def get_client_email(self):
        if self.client:
            email = self.client.user.email
            return email
        else:
            return ""

    def get_staff_email(self):
        if self.va_assigned:
            current_staff = self.va_assigned.through.objects.all()
            staff_emails = " ".join(
                staff.user.email for staff in self.va_assigned.all()
            )
        return staff_emails

    def get_account_files(self):
        account_file = AccountFile.objects.filter(client=self.client)
        account_files = ", ".join(i.url for i in account_file)
        return account_files

    def get_company_client(self):
        if self.caller_interaction_record:
            client = self.caller_interaction_record.company.client
            return client
        elif self.client:
            return self.client

    def save(self, *args, **kwargs):
        if not self.id:
            self.ticket_number = self.create_ticket_number()
            self.client = self.get_company_client()
            self.client_file = self.get_account_files()
            super(JobOrderPostPaid, self).save(*args, **kwargs)
        elif self.id:
            self.ticket_number = self.create_ticket_number()
            self.client = self.get_company_client()
            self.client_file = self.get_account_files()
            self.client_email = self.get_client_email()
            self.staff_email = self.get_staff_email()
            super(JobOrderPostPaid, self).save(*args, **kwargs)


class JobOrderComment(TimeStamped):
    job_order = models.ForeignKey(
        JobOrderPostPaid,
        related_name="job_order_comments",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    comment = models.TextField()

    class Meta:
        ordering = ["created_at"]
