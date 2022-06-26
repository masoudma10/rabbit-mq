import pika
from config import RabbitConfig


class ConnectRabbitServer:

    def __init__(self):
        self.hosting = pika.ConnectionParameters(host=RabbitConfig.host, port=RabbitConfig.port)
