from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now


class Code(models.Model):
    date_created = models.DateTimeField(default=now())
    code = models.CharField(max_length=10)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.code

class UserAttrib(models.Model):
    date_created = models.DateTimeField(default=now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imgpath = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    date_created = models.DateTimeField(default=now())
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='source')
    toUser = models.ForeignKey(User, on_delete=models.CASCADE,related_name='destination')
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.fromUser.username