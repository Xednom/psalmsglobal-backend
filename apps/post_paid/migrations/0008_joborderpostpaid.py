# Generated by Django 3.2.4 on 2021-07-06 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_client_hourly_rate_currency'),
        ('post_paid', '0007_auto_20210628_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOrderPostPaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_file', models.CharField(blank=True, max_length=500)),
                ('client_email', models.EmailField(blank=True, max_length=254)),
                ('staff_email', models.CharField(blank=True, max_length=500)),
                ('ticket_number', models.CharField(blank=True, max_length=100)),
                ('request_date', models.DateField()),
                ('due_date', models.DateField()),
                ('job_title', models.CharField(max_length=250)),
                ('job_description', models.TextField()),
                ('client_notes', models.TextField(blank=True)),
                ('va_notes', models.TextField(blank=True)),
                ('management_notes', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('na', 'N/A'), ('job_order_request', 'Job order request'), ('va_processing', 'VA Processing'), ('management_processing', 'Management Processing'), ('verified_job_order', 'Verified Job Order'), ('on_hold', 'On Hold'), ('canceled', 'Canceled'), ('follow_up', 'Follow up'), ('dispute', 'Dispute'), ('complete', 'Complete'), ('under_quality_review', 'Under Quality Review'), ('daily_tasks', 'Daily Tasks'), ('weekly_tasks', 'Weekly Tasks'), ('monthly_tasks', 'Monthly Tasks'), ('redo', 'Redo'), ('pending', 'Pending'), ('request_for_posting', 'Request for Posting'), ('mark_as_sold_request', 'Mark as Sold Request'), ('initial_dd_processing', 'Initial DD Processing'), ('initial_dd_complete', 'Initial DD Complete'), ('dd_call_out_processing', 'DD Call Out Processing'), ('dd_call_out_complete', 'DD Call Out Complete'), ('duplicate_request', 'Duplicate Request')], default='na', max_length=100)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('total_time_consumed', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('url_of_the_completed_jo', models.TextField(blank=True)),
                ('caller_interaction_record', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interaction_job_orders', to='post_paid.interactionrecord')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients_job_orders', to='authentication.client')),
                ('va_assigned', models.ManyToManyField(blank=True, related_name='vas_job_orders', to='authentication.Staff')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]