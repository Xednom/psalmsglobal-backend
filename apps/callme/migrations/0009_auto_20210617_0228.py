# Generated by Django 3.2.4 on 2021-06-17 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callme', '0008_auto_20210614_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='input_question',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value_text',
            field=models.TextField(blank=True),
        ),
    ]
