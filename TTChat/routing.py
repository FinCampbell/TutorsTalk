from django.conf.urls import url
from .consumers import TTChatCons

websocket_urlpatterns = [
  url(r'^ws/TTChat/(?P<room_name>[^/]+)/$', TTChatCons),
]