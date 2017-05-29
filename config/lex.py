import os

class Lex(Object):
    @staticmethod
    def getBotName(self):
        return os.getenv('LEX_BOT_NAME')
    
    @staticmethod
    def getBotAlias(self):
        return os.getenv('LEX_BOT_ALIAS')

    @staticmethod
    def getUserId(self):
        return os.getenv('LEX_USER_ID')
