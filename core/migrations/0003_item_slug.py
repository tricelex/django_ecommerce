# Generated by Django 3.1.5 on 2021-01-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_auto_20210108_1358"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="slug",
            field=models.SlugField(default="test-product"),
            preserve_default=False,
        ),
    ]
