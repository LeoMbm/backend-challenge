# Generated by Django 4.1 on 2022-08-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_countries_country_logs_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]