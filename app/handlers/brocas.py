from config.brocas import Brocas as BrocasConfig
import requests

class Brocas(object):
    def textToSpeech(self, text):      
        payload = {"text": text}
        
        return requests.post(BrocasConfig.getURL(), json=payload);