import json
import math
import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    session_user_color = str()

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
        data = json.loads(text_data)
        type = data["type"]
        msg = {}
        if type == "chat_message":
            msg = {
                'type': 'chat_message',
                'message': data['message'],
                'username': data['username']
            }
        elif type == "join_message":
            msg = {
                'type': 'join_message',
                'username': data['username']
            }

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, msg)

    # Receive message from room group
    def join_message(self, event):
        self.session_user_color = "#%06x" % random.randint(0, 0xFFFFFF)
        message = "join to the chat"
        username = event['username']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            "color": self.session_user_color
        }))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            "color": self.session_user_color
        }))
