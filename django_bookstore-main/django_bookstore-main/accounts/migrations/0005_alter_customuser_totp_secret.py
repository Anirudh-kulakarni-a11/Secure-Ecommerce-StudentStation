# Generated by Django 4.1.5 on 2023-12-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_customuser_is_2fa_enabled_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="totp_secret",
            field=models.CharField(
                default="FZSVYE373YEVBEMX64WHO35YWLPUW5WC", max_length=100
            ),
        ),
    ]