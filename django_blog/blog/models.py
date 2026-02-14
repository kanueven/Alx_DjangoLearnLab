from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    tags = TaggableManager(blank=True)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    prof_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print("=== create_user_profile signal triggered ===")
    if created:
        Profile.objects.create(user=instance)
        print(f"Profile created for user: {instance.username}")