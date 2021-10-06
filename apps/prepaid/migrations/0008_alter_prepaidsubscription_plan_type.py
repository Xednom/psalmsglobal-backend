# Generated by Django 3.2.7 on 2021-10-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prepaid', '0007_interactionrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prepaidsubscription',
            name='plan_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prepaid_plan_types', to='prepaid.subscriptiontype'),
        ),
    ]
