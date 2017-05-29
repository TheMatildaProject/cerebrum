import os

class AWS():
    @staticmethod
    def getAccessKeyId():
        return os.getenv('AWS_ACCESS_KEY_ID')
    @staticmethod
    def getSecretKeyId():
        return os.getenv('AWS_SECRET_KEY_ID')
    @staticmethod
    def getRegionName():
        return os.getenv('AWS_REGION_NAME')