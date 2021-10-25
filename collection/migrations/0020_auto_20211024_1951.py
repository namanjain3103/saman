# Generated by Django 2.2 on 2021-10-24 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0019_auto_20211023_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='delivered_on',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
        migrations.AlterField(
            model_name='accessory',
            name='expected_delivery',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
        migrations.AlterField(
            model_name='men',
            name='delivered_on',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
        migrations.AlterField(
            model_name='men',
            name='expected_delivery',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
        migrations.AlterField(
            model_name='women',
            name='delivered_on',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
        migrations.AlterField(
            model_name='women',
            name='expected_delivery',
            field=models.DateField(default=datetime.date(2021, 11, 3)),
        ),
    ]
