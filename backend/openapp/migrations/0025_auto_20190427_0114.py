# Generated by Django 2.1.7 on 2019-04-26 17:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0024_auto_20190427_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 17, 14, 52, 810449, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 17, 14, 52, 810449, tzinfo=utc)),
        ),
    ]
