# Generated by Django 5.0.3 on 2024-04-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100)),
                (
                    "contact",
                    models.CharField(max_length=100, verbose_name="Phone Number"),
                ),
                ("time", models.TimeField()),
                ("notes", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
