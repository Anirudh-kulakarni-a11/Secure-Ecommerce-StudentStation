# Generated by Django 4.1.5 on 2023-12-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_alter_customuser_totp_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="totp_secret",
            field=models.CharField(
                default="JR3NP3FRUAPN4VGEP5Z3GMGEXMJYRBXC", max_length=100
            ),
        ),
    ]
