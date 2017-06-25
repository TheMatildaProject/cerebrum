from app.intents.intent import Intent
import random

class BadWords(Intent):
    def handle(self):
        return self._getRandomResponse()

    def _getRandomResponse(self):
        return random.choice(self._getResponses())

    def _getResponses(self):
        return [
            'Hey, show some respect!',
            'Oh boy...',
            "How is your momma doing?"
        ]
