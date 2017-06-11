from app.intents.intent import Intent
import random

class ChitChat(Intent):
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

    