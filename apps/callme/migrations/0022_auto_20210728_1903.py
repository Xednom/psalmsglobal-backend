# Generated by Django 3.2.5 on 2021-07-28 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('callme', '0021_auto_20210723_0836'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-client'], 'verbose_name': 'Owners Company List', 'verbose_name_plural': 'Owners Company List'},
        ),
        migrations.AlterModelOptions(
            name='crm',
            options={'ordering': ['-company'], 'verbose_name': 'Type of Clients CRM', 'verbose_name_plural': 'Type of Clients CRM'},
        ),
        migrations.AlterModelOptions(
            name='form',
            options={'verbose_name': 'List of Scripts per Company'},
        ),
        migrations.AlterModelOptions(
            name='offerstatus',
            options={'verbose_name': 'Update Offer Status', 'verbose_name_plural': 'Update Offer Status'},
        ),
        migrations.AlterModelOptions(
            name='phonesystem',
            options={'ordering': ['-company'], 'verbose_name': 'List of Sub Numbers'},
        ),
        migrations.AlterModelOptions(
            name='propertyinfo',
            options={'verbose_name': 'Sellers Property Inventory List', 'verbose_name_plural': 'Sellers Property Inventory List'},
        ),
        migrations.AlterModelOptions(
            name='vodaconnectlinetype',
            options={'verbose_name': 'VodaConnect Line Category', 'verbose_name_plural': 'Vodaconnect Line Category'},
        ),
        migrations.AlterModelOptions(
            name='vodaconnectplan',
            options={'verbose_name': 'VodaConnect Plan Type', 'verbose_name_plural': 'VodaConnect Plan Type'},
        ),
    ]
