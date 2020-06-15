from django.conf.urls import url
from .views import Example_View, Profile_View, signup
from TTChat.views import ChatRoomIndex


urlpatterns = [
  url(r'^$', Example_View.as_view()),
  url(r'profile/', Profile_View.as_view(), name="profile"),
  url(r'signup/$', signup, name="signup"),
  url(r'TTChat/', ChatRoomIndex, name="TTChat"),
]

