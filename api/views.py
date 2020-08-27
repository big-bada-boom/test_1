from django.shortcuts import render
from rest_framework.response import Response
from .models import User, Chat, Message
from .serializers import UserSerializer, ChatSerializer, MessageSerializer
from rest_framework import status
from rest_framework.views import APIView

class APIUser(APIView):
    def post(self, request):
        seriailzer = UserSerializer(data=request.data)
        if seriailzer.is_valid():
            if 'username' in request.data:
                try:
                    seriailzer.save()
                except:
                    return Response(seriailzer.errors, 
                        status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'id':seriailzer.data['pk']}, 
                                    status.HTTP_201_CREATED)
        return Response(seriailzer.errors, 
                        status.HTTP_400_BAD_REQUEST)

class APIChat(APIView):
    def post(self, request):
        seriailzer = ChatSerializer(data=request.data)
        if seriailzer.is_valid():
            if 'name' and 'users' in request.data:
                try:
                    seriailzer.save()
                except:
                    return Response(seriailzer.errors, 
                        status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'id':seriailzer.data['pk']}, 
                                    status.HTTP_201_CREATED)
        return Response(seriailzer.errors, 
                        status.HTTP_400_BAD_REQUEST)

class APIMessage(APIView):
    def post(self, request):
        seriailzer = MessageSerializer(data=request.data)
        if seriailzer.is_valid():
            if 'chat' and 'author' and 'text' in request.data:
                try:
                    seriailzer.save()
                except:
                    return Response(seriailzer.errors, 
                        status.HTTP_400_BAD_REQUEST)
                else:
                    print(type(seriailzer.data))
                    return Response({'id':seriailzer.data['pk']}, 
                                    status.HTTP_201_CREATED)
        return Response(seriailzer.errors, 
                        status.HTTP_400_BAD_REQUEST)

class APIGetChat(APIView):
    def post(self, request):
        if type(request.data) != int:
            if 'user' in request.data:
                chats = Chat.objects.filter(users=request.data['user'])
                print(request.data)
                seriailzer = ChatSerializer(chats.order_by('-created_at'), many=True)
                return Response(seriailzer.data, 
                                status.HTTP_201_CREATED)
        return Response('400 Bad Request')

class APIGetMessage(APIView):
    def post(self, request):
        if type(request.data) != int:
            if 'chat' in request.data:
                messages = Message.objects.filter(chat=request.data['chat'])
                print(request.data)
                seriailzer = MessageSerializer(messages.order_by('-created_at'), many=True)
                return Response(seriailzer.data, 
                                status.HTTP_201_CREATED)
        return Response('400 Bad Request')


# Create your views here.
