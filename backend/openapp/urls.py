from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate-code', views.generateCode, name='generateCode'),
    path('register', views.register, name='register'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name='logoutUser'),

    path('profile/<slug:college>', views.collegeprofile, name='collegeprofile'),
    path('chat/<slug:college>', views.collegechat, name='collegechat'),

    path('chat', views.chat, name='chat'),

    path('appoint/<slug:college>', views.appoint, name='appoint'),
    path('getAppointmentSchedules/<slug:college>', views.getAppointmentSchedules, name='getAppointmentSchedules'),
    path('setAppointmentSchedule', views.setAppointmentSchedule, name='setAppointmentSchedule'),
    path('cancelAppointment', views.cancelAppointment, name='cancelAppointment'),

    # path('hasCode', views.hasCode, name='hasCode'),
    path('getCodeStatus', views.getCodeStatus, name='getCodeStatus'),
    # path('setCodeAsUsed', views.setCodeAsUsed, name='setCodeAsUsed'),
]