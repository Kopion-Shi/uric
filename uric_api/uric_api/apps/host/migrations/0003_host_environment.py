# Generated by Django 5.1.1 on 2024-09-18 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("conf_center", "0001_initial"),
        ("host", "0002_pkeymodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="host",
            name="environment",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="conf_center.environment",
                verbose_name="从属环境",
            ),
        ),
    ]
