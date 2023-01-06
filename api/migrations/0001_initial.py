# Generated by Django 4.1.4 on 2023-01-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("post", models.CharField(blank=True, max_length=250)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
