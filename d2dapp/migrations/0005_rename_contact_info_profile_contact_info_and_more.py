# Generated by Django 4.1 on 2022-09-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("d2dapp", "0004_rename_role_profile_userrole"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile", old_name="contact_info", new_name="Contact_info",
        ),
        migrations.RenameField(
            model_name="profile", old_name="email", new_name="Email",
        ),
        migrations.RenameField(
            model_name="profile", old_name="fullname", new_name="Fullname",
        ),
        migrations.RenameField(
            model_name="profile", old_name="location", new_name="Location",
        ),
        migrations.RenameField(
            model_name="profile", old_name="password", new_name="Password",
        ),
        migrations.RenameField(
            model_name="userrole", old_name="role", new_name="Role",
        ),
    ]
