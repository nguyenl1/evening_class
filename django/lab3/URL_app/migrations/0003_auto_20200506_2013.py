# Generated by Django 3.0.6 on 2020-05-07 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('URL_app', '0002_auto_20200506_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urlform',
            old_name='enter_url',
            new_name='url_link',
        ),
    ]
