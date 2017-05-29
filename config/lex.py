import os

class Lex():
    @staticmethod
    def getBotName():
        return os.getenv('LEX_BOT_NAME')
    
    @staticmethod
    def getBotAlias():
        return os.getenv('LEX_BOT_ALIAS')

    @staticmethod
    def getUserId():
        return os.getenv('LEX_USER_ID')
