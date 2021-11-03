# Generated by Django 3.2.8 on 2021-11-02 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='order',
            name='deliveredAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paidAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
