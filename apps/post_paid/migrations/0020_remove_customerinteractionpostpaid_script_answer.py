# Generated by Django 3.2.5 on 2021-08-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_paid', '0019_auto_20210812_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinteractionpostpaid',
            name='script_answer',
        ),
    ]