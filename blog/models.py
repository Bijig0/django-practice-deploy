from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tutorial(models.Model):
    name = models.CharField(max_length=40)
    on_del = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

