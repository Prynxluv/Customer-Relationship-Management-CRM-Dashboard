# Generated by Django 5.0.8 on 2024-08-17 10:29

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0003_alter_customer_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                always_update=True,
                editable=False,
                null=True,
                populate_from="full_name",
                unique=True,
            ),
        ),
    ]
