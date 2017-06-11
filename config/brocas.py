import os

class Brocas():
    @staticmethod
    def getURL():
        return os.getenv('BROCAS_URL')