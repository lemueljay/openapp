# Generated by Django 2.1.7 on 2019-04-30 14:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0027_auto_20190427_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 14, 17, 5, 548888, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 14, 17, 5, 548888, tzinfo=utc)),
        ),
    ]
