# Generated by Django 3.1.5 on 2021-01-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description for a dummy product...'),
            preserve_default=False,
        ),
    ]
