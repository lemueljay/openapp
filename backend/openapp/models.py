from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now
import datetime

class Code(models.Model):
    date_created = models.DateTimeField(default=now())
    code = models.CharField(max_length=10)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class UserAttrib(models.Model):
    date_created = models.DateTimeField(default=now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imgpath = models.CharField(max_length=100, default='img/001.png')
    course = models.CharField(max_length=100, blank=True)
    birthday = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    date_created = models.DateTimeField(default=datetime.datetime.now)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='source')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name='destination')
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.sender.username

class Schedule(models.Model):
    counselor = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.CharField(max_length=1000, blank=True, default='')
    date = models.DateField(default=datetime.date.today)
    time = models.CharField(max_length=1000,default=None)
    
    def __str__(self):
        return str(self.date) + ' ' + str(self.time)


class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    info_name = models.CharField(max_length=1000,default=None)
    info_id = models.CharField(max_length=1000,default=None)
    info_college = models.CharField(max_length=1000,default=None)
    info_yrcourse = models.CharField(max_length=1000,default=None)
    info_gender = models.CharField(max_length=1000,default=None)
    info_location = models.CharField(max_length=1000,default=None)

    def __str__(self):
        return str(self.info_name) + ' ' + str(self.schedule.date) + ' ' + str(self.schedule.time)