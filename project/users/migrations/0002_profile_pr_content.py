# Generated by Django 5.1.3 on 2024-11-21 03:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="PR_content",
            field=models.TextField(
                default="Default content",
                validators=[django.core.validators.MaxLengthValidator(75)],
            ),
        ),
    ]
