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
    seen = models.CharField(max_length=1000, default='UNSEEN')

    def __str__(self):
        return self.sender.username

class Schedule(models.Model):
    counselor = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.CharField(max_length=1000, blank=True, default='')
    date = models.DateField(default=datetime.date.today)
    time = models.CharField(max_length=1000,default=None)
    status = models.CharField(max_length=1000,default=None)
    
    # Approval status
    approved = models.CharField(max_length=1000, blank=True, default='NOT_APPROVED')

    info_name = models.CharField(max_length=1000,default=None,null=True)
    info_id = models.CharField(max_length=1000,default=None,null=True)
    info_college = models.CharField(max_length=1000,default=None,null=True)
    info_yrcourse = models.CharField(max_length=1000,default=None,null=True)
    info_studentyear = models.CharField(max_length=1000,default=None,null=True)
    info_gender = models.CharField(max_length=1000,default=None,null=True)
    info_location = models.CharField(max_length=1000,default=None,null=True)
    
    def __str__(self):
        return str(self.date) + ' ' + str(self.time)

class Notification(models.Model):

    date_created = models.DateTimeField(default=datetime.datetime.now)

    sourceUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sourceUser')
    destUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destUser')

    # Type of notification - 
    # APPOINTMENT | MESSAGE
    notifType = models.CharField(max_length=1000,default=None,null=True)

    # Foreign ID - Schedule or Chat
    notifId = models.CharField(max_length=1000,default=None,null=True)

    # Read or unread
    status = models.CharField(max_length=1000,default=None,null=True)

    # Message to be displayed
    message = models.CharField(max_length=1000,default=None,null=True)