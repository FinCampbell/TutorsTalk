from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from home.models import Profile

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
  last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
  email = forms.EmailField(max_length=24, help_text="Required")
  
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

#class ProfileForm(forms.ModelForm):
  #class Meta:
    #model = Profile
    #field = avatar
    
    #def clean_avatar(self):
      #avatar = self.cleaned_data['avatar']
      
      #try:
        #w, h = get_image_dimensions(avatar)
        
        #max_width = max_height = 100
        #if w > max_width or h > max_height:
          #raise forms.ValidationError('Please Use Image Smaller than %s by %s pixels.' % (max_width, max_height))
      
      #except AttributeError:
        #pass
      
      #return avatar