# Generated by Django 3.1.2 on 2021-01-22 00:24

import multiselectfield.db.fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("authentication", "0017_remove_fleetup_permission"),
        ("inactivity", "0002_add_manage_leave_perm"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inactivitypingconfig",
            options={
                "default_permissions": (),
                "verbose_name": "inactivity policy",
                "verbose_name_plural": "inactivity policies",
            },
        ),
        migrations.AlterField(
            model_name="inactivitypingconfig",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="Groups subject to the inactivity policy. If empty, applies to all groups.",
                related_name="_inactivitypingconfig_groups_+",
                to="auth.Group",
            ),
        ),
        migrations.AlterField(
            model_name="inactivitypingconfig",
            name="name",
            field=models.CharField(
                help_text="Internal name for the inactivity policy. Must be unique.",
                max_length=48,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="inactivitypingconfig",
            name="states",
            field=models.ManyToManyField(
                blank=True,
                help_text="States subject to the inactivity policy. If empty, applies to all states.",
                related_name="_inactivitypingconfig_states_+",
                to="authentication.State",
            ),
        ),
        migrations.CreateModel(
            name="Webhook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="short name to identify this webhook",
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    "notification_types",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            (1, "Inactive User"),
                            (10, "Leave of Absence - Created"),
                            (11, "Leave of Absence - Approved"),
                        ],
                        help_text="only notifications of the selected types are sent to this webhook",
                        max_length=7,
                    ),
                ),
                (
                    "url",
                    models.CharField(
                        help_text="URL of this webhook, e.g. https://discordapp.com/api/webhooks/123456/abcdef",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "webhook_type",
                    models.IntegerField(
                        choices=[(1, "Discord Webhook")],
                        default=1,
                        help_text="type of this webhook",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="whether notifications are currently sent to this webhook",
                    ),
                ),
                (
                    "ping_configs",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The inactivity policies to alert for. If left blank, all policies are alerted for.",
                        to="inactivity.InactivityPingConfig",
                    ),
                ),
            ],
        ),
    ]
