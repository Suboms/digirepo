# Generated by Django 4.2 on 2023-05-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_password2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password2",
            field=models.CharField(
                blank=True,
                default="",
                max_length=128,
                null=True,
                verbose_name="Confirm Password",
            ),
        ),
    ]
