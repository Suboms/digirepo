# Generated by Django 4.2 on 2023-05-13 15:20

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0007_alter_schools_logo_alter_schools_website"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schools",
            name="country",
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
