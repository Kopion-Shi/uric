# Generated by Django 3.0 on 2024-02-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
