# Generated by Django 3.0.6 on 2020-05-07 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URL_app', '0003_auto_20200506_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlform',
            name='code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
