# Generated by Django 3.0.5 on 2020-04-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20200427_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='desp',
            field=models.CharField(max_length=250),
        ),
    ]
