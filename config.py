import os


class RabbitConfig:

    host = os.environ.get('RABBIT_HOST')
    port = os.environ.get('PORT')

