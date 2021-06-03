# Generated by Django 3.2.3 on 2021-06-03 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_account_type'),
        ('prepaid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbalance',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prepaid_client_account_balance', to='authentication.client'),
        ),
    ]