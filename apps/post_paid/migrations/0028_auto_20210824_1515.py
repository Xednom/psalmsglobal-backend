# Generated by Django 3.2.5 on 2021-08-24 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_paid', '0027_auto_20210824_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutesreport',
            name='ci_minutes_overview',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='minutesreport',
            name='general_request_total_minutes',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='minutesreport',
            name='monthly_usage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='minutesreport',
            name='total_minutes_unused',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=19, null=True),
        ),
    ]
