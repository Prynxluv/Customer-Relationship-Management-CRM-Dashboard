# Generated by Django 5.0.8 on 2024-08-10 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Report",
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
                ("full_name", models.CharField(max_length=100, null=True)),
                ("phone", models.PositiveIntegerField(null=True)),
                ("email", models.CharField(max_length=100, null=True)),
                ("message", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="TreatmentList",
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
                ("treatment_name", models.CharField(max_length=200, null=True)),
                ("extra_note", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Information",
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
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("age", models.PositiveIntegerField(null=True)),
                ("address_1", models.CharField(max_length=300, null=True)),
                ("address_2", models.CharField(max_length=300, null=True)),
                ("city", models.CharField(max_length=255, null=True)),
                ("county", models.CharField(max_length=255, null=True)),
                ("postcode", models.CharField(max_length=20, null=True)),
                ("country", models.CharField(max_length=100, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=1000, null=True, unique=True
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customers_name",
                        to="crm.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SkinCareInquiry",
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
                (
                    "hair_coloring",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=10, null=True
                    ),
                ),
                ("hair_coloring_details", models.TextField(max_length=1000, null=True)),
                (
                    "scalp_issues",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=10, null=True
                    ),
                ),
                ("scalp_issues_details", models.TextField(max_length=1000, null=True)),
                (
                    "skin_allergy",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=10, null=True
                    ),
                ),
                ("skin_allergy_details", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.customer",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Skin Care Inquiries",
            },
        ),
        migrations.CreateModel(
            name="SkinCareReport",
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
                (
                    "allergic_reaction",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=10, null=True
                    ),
                ),
                (
                    "proceed_service",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=10, null=True
                    ),
                ),
                ("observation", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.customer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Treatment",
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
                ("treatment_note", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.customer",
                    ),
                ),
                (
                    "treatment_list",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.treatmentlist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ScheduleAppointment",
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
                (
                    "schedule",
                    models.CharField(
                        choices=[
                            ("9am to 10am", "9am to 10am"),
                            ("10am to 11am", "10am to 11am"),
                            ("11am to 12pm", "11am to 12pm"),
                            ("12pm to 1pm", "12pm to 1pm"),
                            ("1pm to 2pm", "1pm to 2pm"),
                            ("2pm to 3pm", "2pm to 3pm"),
                            ("3pm to 4pm", "3pm to 4pm"),
                            ("4pm to 5pm", "4pm to 5pm"),
                            ("5pm to 6pm", "5pm to 6pm"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("appointment_note", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.customer",
                    ),
                ),
                (
                    "treatment_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.treatmentlist",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookAppointment",
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
                ("full_name", models.CharField(max_length=100, null=True)),
                ("phone", models.PositiveIntegerField(null=True)),
                ("email", models.CharField(max_length=100, null=True)),
                ("address", models.CharField(max_length=100, null=True)),
                (
                    "schedule",
                    models.CharField(
                        choices=[
                            ("9am to 10am", "9am to 10am"),
                            ("10am to 11am", "10am to 11am"),
                            ("11am to 12pm", "11am to 12pm"),
                            ("12pm to 1pm", "12pm to 1pm"),
                            ("1pm to 2pm", "1pm to 2pm"),
                            ("2pm to 3pm", "2pm to 3pm"),
                            ("3pm to 4pm", "3pm to 4pm"),
                            ("4pm to 5pm", "4pm to 5pm"),
                            ("5pm to 6pm", "5pm to 6pm"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("Monday", "Monday"),
                            ("Tuesday", "Tuesday"),
                            ("Wednesday", "Wednesday"),
                            ("Thursday", "Thursday"),
                            ("Friday", "Friday"),
                            ("Saturday", "Saturday"),
                            ("Sunday", "Sunday"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("message", models.TextField(max_length=1000, null=True)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "treatment_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="crm.treatmentlist",
                    ),
                ),
            ],
        ),
    ]
