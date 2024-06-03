# Generated by Django 4.1.3 on 2023-03-07 11:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_company_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="companyuser",
            name="company",
        ),
        migrations.RemoveField(
            model_name="companyuser",
            name="user",
        ),
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.AddField(
            model_name="user",
            name="company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.company",
            ),
            preserve_default=False,
        ),
    ]
