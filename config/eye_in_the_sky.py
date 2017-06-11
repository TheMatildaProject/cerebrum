import os

class EyeInTheSky():
    @staticmethod
    def getWeatherAPIUrl():
        return os.getenv('EYE_IN_THE_SKY_URL')