# Generated by Django 3.2.5 on 2021-08-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_paid', '0021_alter_joborderpostpaid_total_time_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinteractionpostpaid',
            name='email',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
