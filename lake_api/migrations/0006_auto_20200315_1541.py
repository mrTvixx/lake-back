# Generated by Django 3.0.4 on 2020-03-15 15:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lake_api', '0005_auto_20200221_1929'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 15, 15, 41, 22, 18832, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='data_file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
