from django.urls import path
from .views import APIUser, APIChat, APIMessage, APIGetChat, APIGetMessage

urlpatterns = [
    path('users/add', APIUser.as_view()),
    path('chats/add', APIChat.as_view()),
    path('messages/add', APIMessage.as_view()),
    path('chats/get', APIGetChat.as_view()),
    path('messages/get', APIGetMessage.as_view()),
]
