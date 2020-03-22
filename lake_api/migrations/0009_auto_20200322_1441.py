# Generated by Django 3.0.4 on 2020-03-22 14:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lake_api', '0008_auto_20200322_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='by_admin',
            field=models.BooleanField(blank=True, default=True, verbose_name='От имени админа'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=2500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 22, 14, 41, 34, 202392, tzinfo=utc)),
        ),
    ]
