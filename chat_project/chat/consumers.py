import json
import math
import random

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    session_user_color = {}

    @staticmethod
    def rnd_color():
        return "#%06x" % random.randint(0, 0xFFFFFF)

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        ChatConsumer.session_user_color.setdefault(self.room_name, {}).setdefault(self.channel_name, {})

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        ChatConsumer.session_user_color[self.room_name].pop(self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)

        type = data["type"]
        username = data['username']
        msg = {
            'type': type,
            'username': username
        }
        if type == "join_message":
            # generate and save username color to chanel
            ChatConsumer.session_user_color[self.room_name][self.channel_name][username] = ChatConsumer.rnd_color()
        elif type == "chat_message":
            msg["message"] = data['message']

        msg["color"] = ChatConsumer.session_user_color[self.room_name][self.channel_name][username]

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, msg)

    # Receive join_message from room group
    def join_message(self, event):
        message = "join to the chat"
        username = event['username']
        color = event["color"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            "color": color
        }))

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        color = event["color"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            "color": color
        }))
