# Generated by Django 4.1 on 2022-09-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("d2dapp", "0006_rename_contact_info_profile_contact_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profileimage",
            field=models.ImageField(
                default="media/default.png", upload_to="profile_images"
            ),
        ),
    ]