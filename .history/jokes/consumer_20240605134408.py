from channels.generic.websocket import AsyncWebsocketConsumer



class JokesConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add('jokes',self.channel_name)
        await super().accept()
    
    async def disconnect(self):
        await self.channel_layer.group_discard('jokes',self.channel_name)
    
    async def send_jokes(self,event):
        text = event['text']
        await self.send(text)
    