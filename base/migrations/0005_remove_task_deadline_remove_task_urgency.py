# Generated by Django 4.2.6 on 2023-12-17 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_task_urgency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='task',
            name='urgency',
        ),
    ]
