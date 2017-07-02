from app.intents.intent import Intent
import random

class Banter(Intent):
    def handle(self):
        return self._getRandomResponse()

    def _getRandomResponse(self):
        return random.choice(self._getResponses())

    def _getResponses(self):
        return [
            'HAHAHA',
            'Very funny...',
            'I feel like I should be laughing too, but I have no humour.'
        ]

    