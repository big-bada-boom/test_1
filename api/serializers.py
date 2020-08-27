from .models import User, Chat, Message
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'created_at')

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('pk', 'name', 'users', 'created_at')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('pk', 'chat', 'author', 'text', 'created_at')
