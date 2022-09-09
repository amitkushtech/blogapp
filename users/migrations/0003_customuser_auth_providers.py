# Generated by Django 4.1 on 2022-09-09 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_customuser_groups_customuser_is_superuser_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="auth_providers",
            field=models.CharField(
                blank=True, default="email", max_length=20, null=True
            ),
        ),
    ]