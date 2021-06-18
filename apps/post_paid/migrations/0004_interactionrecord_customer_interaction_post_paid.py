# Generated by Django 3.2.4 on 2021-06-18 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_paid', '0003_interactionrecord_ticket_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactionrecord',
            name='customer_interaction_post_paid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer_interaction_post_paid_records', to='post_paid.customerinteractionpostpaid'),
        ),
    ]
