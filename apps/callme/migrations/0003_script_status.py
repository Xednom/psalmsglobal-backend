# Generated by Django 3.2.4 on 2021-06-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callme', '0002_auto_20210611_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
