# Generated by Django 4.1 on 2022-08-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_todo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='show',
            new_name='task',
        ),
    ]
