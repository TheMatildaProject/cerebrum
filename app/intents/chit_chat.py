import random

class ChitChat(object):
    def __init__(self, message):
        message = message

    def handle(self):
        return self._getRandomResponse()

    def _getRandomResponse(self):
        return random.choice(self._getResponses())

    def _getResponses(self):
        return [
            'Hello, how are you?',
            'What is up?',
            "Hello"
        ]

    