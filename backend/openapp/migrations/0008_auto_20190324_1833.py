# Generated by Django 2.1.7 on 2019-03-24 10:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0007_auto_20190324_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 10, 33, 19, 731921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 10, 33, 19, 731921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 10, 33, 19, 731921, tzinfo=utc)),
        ),
    ]
