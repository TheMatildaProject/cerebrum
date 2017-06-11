import os

class EyeInTheSky():
    @staticmethod
    def getURL():
        return os.getenv('EYE_IN_THE_SKY_URL')