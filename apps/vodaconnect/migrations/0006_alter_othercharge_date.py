# Generated by Django 3.2.8 on 2021-12-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vodaconnect', '0005_alter_plansummaryandpayment_date_of_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='othercharge',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
