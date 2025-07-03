# booking/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BookingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'You are connected to Booking WebSocket!'
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("booking_updates", self.channel_name)

    async def receive(self, text_data):
        pass  # No need for client-to-server messages yet

    async def send_booking(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
