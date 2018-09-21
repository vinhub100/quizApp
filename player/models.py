from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User)
    score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Player"
    
    def __str__(self):
        return self.user.username
