from app.handlers.eye_in_the_sky import EyeInTheSky
from app.intents.intent import Intent

class TodaysWeather(Intent):
    message = ""

    def __init__(self, message):
        self.message = message

    def handle(self):
        eits = EyeInTheSky()
        eits.getWeatherForecast("Auckland")
        return "Under construction"

