# Generated by Django 3.1.1 on 2020-09-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Document name"),
                ),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                ("is_in_progress", models.BooleanField(default=False)),
            ],
        ),
    ]