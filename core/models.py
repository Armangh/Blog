from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField(default=False)
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             related_name='comments')

    def __str__(self):
        return self.body[:20]


class Tag(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField('Post', related_name='tags')

    def __str__(self):
        return self.title
