import os

class Brocas():
    @staticmethod
    def getBrocasUrl():
        return os.getenv('BROCAS_URL')