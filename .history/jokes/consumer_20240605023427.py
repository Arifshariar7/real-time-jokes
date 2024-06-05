from channels.generic.websocket import AsyncWebsocketConsumer



class JokesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('jokes',self.channel_name)
        return await super().accept()
    async def disconnect(self, code):
        await self.channel_layer.group_discard('jokes',self.channel_name)
        return await super().disconnect(code)
    