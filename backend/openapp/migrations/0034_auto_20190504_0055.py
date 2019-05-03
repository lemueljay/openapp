# Generated by Django 2.1.7 on 2019-05-03 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0033_auto_20190504_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 16, 55, 0, 522791, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='info_college',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='info_gender',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='info_id',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='info_location',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='info_name',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='info_yrcourse',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 16, 55, 0, 523792, tzinfo=utc)),
        ),
    ]
