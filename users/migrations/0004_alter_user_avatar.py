# Generated by Django 4.1 on 2023-05-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                default="/static/main/image/avatar-default-icon.png",
                upload_to="",
                verbose_name="avatar",
            ),
        ),
    ]
