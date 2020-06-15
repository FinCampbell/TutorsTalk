from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import transaction

from .forms import SignUpForm
from .models import Room, Message

import string
import random

# Functions for later

# Create your views here.

class Example_View(TemplateView):
  template_name = "home/TestHTML.html"
  
class Profile_View(TemplateView):
  template_name = "home/profile.html"
   
def signup(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('/')
  else:
    form = SignUpForm()
  return render(request, 'home/signup.html', {'form' : form})