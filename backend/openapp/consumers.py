from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import datetime

from django.contrib.auth.models import User
from .models import Code, UserAttrib, Message

from .utils import CodeGenerator

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']

        print('USER: ' + str(self.scope['user']))
        senderUser = User.objects.get(username__icontains=sender)
        receiverUser = User.objects.get(username__icontains=receiver)

        data = Message(sender=senderUser, receiver=receiverUser, message=str(message))
        data.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'receiver': receiver,
                'timestamp': str(data.date_created.ctime())
            }
        )

    # Receive message from room group
    def chat_message(self, event):

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender'],
            'receiver': event['receiver'],
            'timestamp': event['timestamp']
        }))