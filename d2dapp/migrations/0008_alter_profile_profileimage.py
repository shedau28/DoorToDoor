# Generated by Django 4.1 on 2022-09-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("d2dapp", "0007_profile_profileimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profileimage",
            field=models.FileField(
                default="media/default.png", upload_to="profile_images"
            ),
        ),
    ]