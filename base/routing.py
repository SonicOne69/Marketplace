from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('ws/chatroom/<str:chatroom>', consumers.MessageChat.as_asgi())
]