# Generated by Django 3.2.4 on 2021-06-23 03:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_paid', '0005_auto_20210621_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerinteractionpostpaid',
            name='script_answer',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
