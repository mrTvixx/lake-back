# Generated by Django 3.0.3 on 2020-02-16 19:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lake_api', '0003_auto_20200216_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 16, 19, 49, 42, 754360, tzinfo=utc)),
        ),
    ]