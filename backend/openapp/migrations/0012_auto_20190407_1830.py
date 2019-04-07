# Generated by Django 2.1.7 on 2019-04-07 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0011_auto_20190407_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
        migrations.AddField(
            model_name='schedule',
            name='dateFrom',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 398529, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='schedule',
            name='dateTo',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 398529, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 397530, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='schedule',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 397530, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 395527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 397530, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 7, 10, 30, 45, 396529, tzinfo=utc)),
        ),
    ]
