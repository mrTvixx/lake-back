# Generated by Django 3.0.3 on 2020-02-21 19:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('lake_api', '0004_auto_20200216_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_pablish',
            new_name='is_publish',
        ),
        migrations.AlterField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 21, 19, 29, 8, 249862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='data_file',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='lake_api.Post'),
        ),
    ]
