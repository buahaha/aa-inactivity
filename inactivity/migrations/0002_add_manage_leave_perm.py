# Generated by Django 3.1.2 on 2021-01-18 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inactivity", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="general",
            options={
                "default_permissions": (),
                "managed": False,
                "permissions": (
                    ("basic_access", "Can access this app"),
                    ("manage_leave", "Can manage leave of absence requests"),
                ),
            },
        ),
    ]
