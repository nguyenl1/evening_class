# Generated by Django 3.0.6 on 2020-05-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0008_remove_checkout_checked_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
