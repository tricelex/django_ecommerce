# Generated by Django 3.1.5 on 2021-01-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_item_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="discount_price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
