from django.contrib import admin

from .models import Code, UserAttrib, Message, Schedule

admin.site.register(Code)
admin.site.register(UserAttrib)
admin.site.register(Message)
admin.site.register(Schedule)