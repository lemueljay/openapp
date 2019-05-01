# Generated by Django 2.1.7 on 2019-05-01 08:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0028_auto_20190430_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='userattrib',
            name='birthday',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userattrib',
            name='course',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userattrib',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 8, 42, 17, 868077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 8, 42, 17, 868578, tzinfo=utc)),
        ),
    ]