# Generated by Django 4.1 on 2022-09-15 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("d2dapp", "0019_rename_profile_product_profile"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="profile", new_name="Profile",
        ),
    ]
