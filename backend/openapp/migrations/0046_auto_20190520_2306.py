# Generated by Django 2.1.7 on 2019-05-20 15:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openapp', '0045_auto_20190518_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('question1', models.CharField(default='', max_length=1000, null=True)),
                ('question2', models.CharField(default='', max_length=1000, null=True)),
                ('question3', models.CharField(default='', max_length=1000, null=True)),
                ('question4', models.CharField(default='', max_length=1000, null=True)),
                ('question5', models.CharField(default='', max_length=1000, null=True)),
                ('question6', models.CharField(default='', max_length=1000, null=True)),
                ('question7', models.CharField(default='', max_length=1000, null=True)),
                ('question8', models.CharField(default='', max_length=1000, null=True)),
                ('question9', models.CharField(default='', max_length=1000, null=True)),
                ('question10', models.CharField(default='', max_length=1000, null=True)),
                ('question11', models.CharField(default='', max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='code',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 15, 6, 45, 502766, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userattrib',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 15, 6, 45, 502766, tzinfo=utc)),
        ),
    ]
