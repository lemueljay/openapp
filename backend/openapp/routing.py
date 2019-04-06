from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url('ws/openapp/chat/(?P<room_name>[^/]+)/', consumers.ChatConsumer),
]