# Generated by Django 4.1 on 2022-08-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='countries',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='logs',
            name='ip',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
