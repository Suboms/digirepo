# Generated by Django 4.2 on 2023-05-31 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_alter_user_password2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="First Name",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Other Names",
            ),
        ),
    ]
