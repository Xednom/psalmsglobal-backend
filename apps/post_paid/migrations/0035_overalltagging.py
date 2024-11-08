# Generated by Django 3.2.8 on 2023-05-11 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_tagging"),
        ("post_paid", "0034_auto_20230510_2105"),
    ]

    operations = [
        migrations.CreateModel(
            name="OverallTagging",
            fields=[
                (
                    "tagging_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.tagging",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("core.tagging",),
        ),
    ]
