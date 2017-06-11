from config.eye_in_the_sky import EyeInTheSky as EyeInTheSkyConfig
import requests

class EyeInTheSky(object):
    def getWeatherForecast(self, city):
        targetUrl = EyeInTheSkyConfig.getURL()

        if (targetUrl == None):
        	return False

        payload = {"city": city}
        return requests.post(EyeInTheSkyConfig.getURL(), json=payload);