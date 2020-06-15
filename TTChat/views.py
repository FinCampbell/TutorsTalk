from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.db import transaction
import json

from home.models import Room

@login_required
def ChatRoomIndex(request):
  return render(request, 'TTChat/index.html', {})

def ChatRoom(request, room_name):
  uniquelab = room_name
  if Room.objects.filter(uniquelab=uniquelab).exists():
    return render(request, 'TTChat/chatroom.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
  else:
    new_room = None
    while not new_room:
      with transaction.atomic():
        new_room = Room.objects.create(uniquelab=uniquelab)
    return render(request, 'TTChat/chatroom.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })