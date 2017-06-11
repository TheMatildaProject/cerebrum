import random

class ChitChatTwo(object):
    def __init__(self, message):
        message = message

    def handle(self):
        return self._getRandomResponse()

    def _getRandomResponse(self):
        return random.choice(self._getResponses())

    def _getResponses(self):
        return [
            'Not too bad',
            "Good, Good, I would be better if I had a real brain though",
            'Alright, cannot complain',
            'Good, thank you'
        ]

    