# Generated by Django 4.2.11 on 2024-04-17 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menuapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menu",
            old_name="cruisine",
            new_name="cuisine",
        ),
    ]