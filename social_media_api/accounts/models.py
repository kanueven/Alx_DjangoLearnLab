from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        #if true,If I follow you → you automatically follow me.
        symmetrical=False,
        related_name='followers',
        blank=True
    )
   

    def __str__(self):
        return self.username
