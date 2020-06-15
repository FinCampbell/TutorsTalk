from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=30)
  info = models.TextField(max_length=300)
  
  def __str__(self):
    return self.title
  
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='uploads/')

class Room(models.Model):
  name = models.TextField()
  uniquelab = models.SlugField(unique=True)
  
class Message(models.Model):
  room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
  handle = models.TextField()
  message = models.TextField()
  timestamp = models.DateTimeField(default=timezone.now, db_index=True)
  
  @property
  def formatted_timestamp(self):
    return self.timestamp.strftime('%H:%M')
  
  def as_dict(self):
    return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()