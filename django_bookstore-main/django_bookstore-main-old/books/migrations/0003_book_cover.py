# Generated by Django 4.1.5 on 2023-01-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="cover",
            field=models.ImageField(default=None, upload_to="covers/"),
            preserve_default=False,
        ),
    ]