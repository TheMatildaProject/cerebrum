from config.echoic_memory import EchoicMemory as EchoicMemoryConfig
import requests

class EchoicMemory(object):
    def playSong(self, song):
        targetUrl = EchoicMemoryConfig.getURL()

        if (targetUrl == None):
        	return False

        payload = {"criteria": song}
        return requests.post(targetUrl + "/search", json=payload);