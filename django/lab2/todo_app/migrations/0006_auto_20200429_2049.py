# Generated by Django 3.0.5 on 2020-04-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_auto_20200428_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
