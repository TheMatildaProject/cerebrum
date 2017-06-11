from app.handlers.eye_in_the_sky import EyeInTheSky
from app.intents.intent import Intent
import json
import re

class TodaysWeather(Intent):
    def handle(Intent):
        eits = EyeInTheSky()
        forecast = eits.getWeatherForecast(Intent._message["slots"]["city"])

        if (forecast == False):
            return "Eye in the sky has not been configured"
        else:
            forecast = json.loads(forecast.text)
            forecastData = forecast["forecast"]
            
            return "It's currently {0} degrees. A maximum of {1} degrees and a minimum of {2} degrees are expected".format(forecastData["temp"], forecastData["temp_max"], forecastData["temp_min"])

   