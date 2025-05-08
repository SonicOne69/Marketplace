from channels.generic.websocket import WebsocketConsumer

class MessageChat(WebsocketConsumer):
    def connect(self):
        self.accept()