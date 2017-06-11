from config.eye_in_the_sky import EyeInTheSky as EyeInTheSkyConfig
import requests

class EyeInTheSky(object):
    def getWeatherForecast(self, text):      
        payload = {"text": text}
        
        return requests.post(EyeInTheSkyConfig.getURL(), json=payload);