from django.conf.urls import url
from .views import ChatRoomIndex, ChatRoom


urlpatterns = [
  url(r'^$', ChatRoomIndex, name='index'),
  url(r'^(?P<room_name>[^/]+)/$', ChatRoom, name='room'),
]