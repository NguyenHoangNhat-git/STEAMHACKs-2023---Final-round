import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models.user import User, Message
import datetime

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        role = self.scope['session']['role']
        current_user = User.get_user_by_id(self.scope['session']['user'])
        if message:
            if role == 'patient':
                new_message = Message(sender=current_user, recipient=current_user.assigned_doctor, content=message, timestamp=datetime.datetime.now())
            else :
                patient = User.get_user_by_id(self.scope['session']['patient'])
                new_message = Message(sender=current_user, recipient=patient, content=message, timestamp=datetime.datetime.now())
            new_message.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message", 
                "message": message, 
                "sender_id": current_user.id
                }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        sender_id = event["sender_id"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "sender_id": sender_id}))