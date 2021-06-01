# Generated by Django 3.2.3 on 2021-06-01 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_user_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_owner_name', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=250)),
                ('business_type', models.CharField(max_length=250)),
                ('company_phone', models.CharField(max_length=250)),
                ('company_email', models.CharField(max_length=250)),
                ('company_complete_address', models.TextField()),
                ('company_forwarding_email', models.CharField(max_length=250)),
                ('paypal_email', models.CharField(max_length=250)),
                ('notes', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_companies', to='authentication.client')),
            ],
            options={
                'ordering': ['-client'],
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('form_title', models.CharField(max_length=250)),
                ('value_text', models.CharField(blank=True, max_length=250)),
                ('value_question', models.TextField(blank=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_attributes', to='callme.attributetype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VodaconnectLineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('line', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VodaconnectPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('range', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_address', models.CharField(blank=True, max_length=250)),
                ('mailing_lists', models.CharField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_scripts', to='callme.company')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_scripts', to='callme.form')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_number', models.BooleanField()),
                ('caller_id_detail', models.TextField()),
                ('original_line', models.CharField(max_length=250)),
                ('call_forwarding_number', models.CharField(max_length=250)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_phone_systems', to='callme.company')),
                ('vodaconnect_line_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vodaconnect_line_type_phone_systems', to='callme.vodaconnectlinetype')),
                ('vodaconnect_plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vodaconnect_plan_phone_systems', to='callme.vodaconnectplan')),
            ],
            options={
                'ordering': ['-company'],
            },
        ),
        migrations.CreateModel(
            name='Crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('crm', models.BooleanField()),
                ('type_of_crm', models.TextField()),
                ('crm_url', models.CharField(max_length=500)),
                ('crm_login', models.CharField(max_length=250)),
                ('notes', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_crms', to='callme.company')),
            ],
            options={
                'ordering': ['-company'],
            },
        ),
    ]
