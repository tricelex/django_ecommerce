# Generated by Django 3.1.5 on 2021-01-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_item_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="quantity",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
