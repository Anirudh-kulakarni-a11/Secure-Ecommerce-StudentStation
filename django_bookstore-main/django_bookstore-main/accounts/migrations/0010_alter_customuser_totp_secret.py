# Generated by Django 4.1.5 on 2023-12-01 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0009_alter_customuser_totp_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="totp_secret",
            field=models.CharField(
                default="Q2JBJCXSJLT3TZG73BBBQGCOUWO2HD7S", max_length=100
            ),
        ),
    ]
