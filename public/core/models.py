from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.
User = get_user_model()
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)  
    profileImg = models.ImageField(upload_to='profile_img', default='blank-picture.png')
    location = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length= 100) 
    files = models.FileField(upload_to='posts')
    caption = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username
    
class Follow(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user