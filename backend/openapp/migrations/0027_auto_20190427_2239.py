# Generated by Django 2.1.7 on 2019-04-27 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0026_auto_20190427_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='counselor',
        ),
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 27, 14, 39, 52, 659715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 27, 14, 39, 52, 659715, tzinfo=utc)),
        ),
    ]
