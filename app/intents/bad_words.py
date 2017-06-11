from app.intents.intent import Intent

class BadWords(Intent):
    _message = ""

    def __init__(self, message):
        self._message = message