import os

class AWS(Object):
    @staticmethod
    def getAccessKeyId(self):
        return os.getenv('AWS_ACCESS_KEY_ID')
    @staticmethod
    def getASecretKeyId(self):
        return os.getenv('AWS_SECRET_KEY_ID')
    @staticmethod
    def getRegionName(self):
        return os.getenv('AWS_REGION_NAME')