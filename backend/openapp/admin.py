from django.contrib import admin

from .models import *

admin.site.register(Code)
admin.site.register(UserAttrib)
admin.site.register(Message)
admin.site.register(Schedule)
admin.site.register(Notification)
admin.site.register(Assessment)