from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('openapp/', include('openapp.urls')),
    path('admin/', admin.site.urls),
]