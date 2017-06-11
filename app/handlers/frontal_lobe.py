# The frontal lobe is responsible for thinking initiation, behaviour, judgment and other things
# On this context, the frontal lobe will swallow Lex's responses and return actionables
# through consulting the configured intents

from app.handlers.brocas import Brocas
from app.intents.bad_words import BadWords
from app.intents.chit_chat import ChitChat
from app.intents.chit_chat_two import ChitChatTwo
from app.intents.play_song import PlaySong
from app.intents.todays_weather import TodaysWeather
from pygame import mixer
import base64
import io
import json
import os
import sys

class FrontalLobe(object):
    def handleResponse(self, message: dict):
        if (message['dialogState'] == 'ReadyForFulfillment'):
            text = self.handleIntent(message)
        else:
            text = message['message']

        brocas = Brocas();
        speechData = brocas.textToSpeech(text).text;
        speech = json.loads(speechData)["sound"]

        self.playResponse(speech)
            

    def handleIntent(self, message):
        intent = message["intentName"]

        # Instantiate intent class from intent string...
        intentClass = eval(intent)(message)

        return intentClass.handle();
    
    def playResponse(self, audio):
        sound = bytes(audio, "utf-8")
        sound = base64.b64decode(sound)

        f = open("temp.ogg",'wb')
        f.write(sound)
        os.fsync(f)
        f.close()

        mixer.init()
        mixer.music.load('temp.ogg')
        mixer.music.play()