# Generated by Django 3.2.8 on 2023-05-31 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("post_paid", "0039_joborderticketsummary_joborderticketsummarycomment"),
        ("authentication", "0006_user_sub_category"),
        ("grading", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TicketSummaryRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("rating", models.IntegerField()),
                ("comment", models.TextField(blank=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="client_ticket_summary_rates",
                        to="authentication.client",
                    ),
                ),
                (
                    "ticket_summary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ticket_summary_rates",
                        to="post_paid.ticketsummary",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
