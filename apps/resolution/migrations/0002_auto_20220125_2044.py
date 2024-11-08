# Generated by Django 3.2.8 on 2022-01-25 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_client_hourly_rate_currency'),
        ('core', '0001_initial'),
        ('resolution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resolution',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff_assigned_resolutions', to='authentication.staff'),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resolution_categories', to='core.resolutioncategory'),
        ),
        migrations.AlterField(
            model_name='resolution',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_resolutions', to='authentication.client'),
        ),
        migrations.AlterField(
            model_name='resolutionconversation',
            name='resolution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resolution_conversations', to='resolution.resolution'),
        ),
        migrations.AlterField(
            model_name='resolutionconversation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_resolution_conversations', to='authentication.staff'),
        ),
    ]
