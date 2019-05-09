# Generated by Django 2.1.7 on 2019-05-09 14:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0040_auto_20190504_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='info_studentyear',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 14, 22, 29, 752380, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 9, 14, 22, 29, 752380, tzinfo=utc)),
        ),
    ]
