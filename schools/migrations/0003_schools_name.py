# Generated by Django 4.2 on 2023-05-13 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0002_alter_schools_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="schools",
            name="name",
            field=models.CharField(default="", max_length=255, unique=True),
        ),
    ]
