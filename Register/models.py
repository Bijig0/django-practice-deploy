from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics',default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}s Profile'



