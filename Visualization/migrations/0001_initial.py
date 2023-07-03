# Generated by Django 4.1.6 on 2023-07-03 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("name", models.CharField(max_length=100)),
                ("domain", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("tech_stack", models.CharField(max_length=100)),
                ("domain", models.CharField(blank=True, max_length=50, null=True)),
                ("subdomain", models.CharField(blank=True, max_length=50, null=True)),
                ("impact", models.TextField(blank=True, null=True)),
                (
                    "organization",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Visualization.organization",
                    ),
                ),
            ],
        ),
    ]