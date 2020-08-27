from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    name = models.CharField(max_length=40, unique=True)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.PROTECT)
    author = models.ManyToManyField(User)
    text = models.TextField()                 
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
