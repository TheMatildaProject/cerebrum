from app.handlers.echoic_memory import EchoicMemory
from app.intents.intent import Intent
import json

class PlaySong(Intent):
    def handle(Intent):
        return Intent._getSongToPlay(Intent._message["slots"]["song"])

    def _getSongToPlay(Intent, song):
        echo = EchoicMemory()
        response = echo.playSong(song)
        
        responseBody = json.loads(response.text)

        return responseBody["video"]