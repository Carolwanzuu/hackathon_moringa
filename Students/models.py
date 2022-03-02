from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from  django.db.models.fields import DateTimeField
from django.db.models.deletion import CASCADE

# Create your models here.
class chamaGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',default=True)
  
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    location = models.CharField(max_length=50, blank=True, null=True)
    chamagroup = models.ForeignKey(chamaGroup, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)


    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
  
  

class Message(models.Model):
  title = models.CharField(max_length=100, blank=True, null=True)
  description = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)
  group = models.ForeignKey(chamaGroup, on_delete=CASCADE, null=True)
  creator = models.ForeignKey(User, on_delete=CASCADE)
  def __str__(self):
      return self.title

class Response(models.Model):
  message = models.ForeignKey(Message, on_delete = models.CASCADE)
  creator = models.ForeignKey(User, on_delete=CASCADE)
  reply = models.TextField()
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.message
  def save_response(self):
    self.save()
  @classmethod
  def get_response(cls, message_id):
    return cls.objects.filter(message = message_id).all()
  @classmethod
  def get_groups(cls):
    try:
      groups = cls.objects.all()
    except cls.DoesNotExist:
      groups = None
    return groups