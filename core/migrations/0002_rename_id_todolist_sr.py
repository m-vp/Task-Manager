# Generated by Django 5.0.1 on 2024-01-29 12:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todolist",
            old_name="id",
            new_name="sr",
        ),
    ]
