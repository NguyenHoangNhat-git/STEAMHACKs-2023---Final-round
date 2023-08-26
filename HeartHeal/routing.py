from django.urls import path
from django.urls import re_path
# from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat-room/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    # url(r'^ws/chat-room/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
    # path('ws/chat/<int:room_id>/', consumers.ChatConsumer.as_asgi()),
]