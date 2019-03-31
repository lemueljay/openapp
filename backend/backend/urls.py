from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    url("", include('django_socketio.urls')),
    path('openapp/', include('openapp.urls')),
    path('admin/', admin.site.urls),
]