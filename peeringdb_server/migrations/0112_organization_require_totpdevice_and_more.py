# Generated by Django 4.2 on 2023-06-24 04:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0111_update_carrierfac_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="require_2fa",
            field=models.BooleanField(
                default=False,
                help_text="Require users in your organization to activate 2FA.",
            ),
        ),
        migrations.AlterField(
            model_name="oauthapplication",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="organizationapikey",
            name="hashed_key",
            field=models.CharField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name="organizationapikey",
            name="id",
            field=models.CharField(
                editable=False,
                max_length=150,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="userapikey",
            name="hashed_key",
            field=models.CharField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name="userapikey",
            name="id",
            field=models.CharField(
                editable=False,
                max_length=150,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
