# Generated by Django 4.1 on 2023-05-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_news_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="views",
            field=models.IntegerField(default=0, verbose_name="Кол-во просмотров"),
        ),
    ]
