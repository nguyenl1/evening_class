# Generated by Django 3.0.6 on 2020-05-07 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=200)),
                ('enter_url', models.CharField(max_length=500)),
            ],
        ),
    ]
