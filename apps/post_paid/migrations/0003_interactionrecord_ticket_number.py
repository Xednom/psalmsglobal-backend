# Generated by Django 3.2.4 on 2021-06-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_paid', '0002_auto_20210611_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactionrecord',
            name='ticket_number',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
