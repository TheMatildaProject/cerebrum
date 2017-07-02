import os

class EchoicMemory():
    @staticmethod
    def getURL():
        return os.getenv('ECHOIC_MEMORY_URL')