# Generated by Django 4.1.5 on 2023-12-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_alter_customuser_totp_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="totp_secret",
            field=models.CharField(
                default="D4A2PUYJPO4MHKFWKPMNURTF7625JKD4", max_length=100
            ),
        ),
    ]