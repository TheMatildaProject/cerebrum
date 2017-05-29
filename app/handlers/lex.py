import boto3, json
from config.aws import AWS as AWSConfig
from config.lex import Lex as LexConfig

class Lex(object):
    def __init__(self):
        self.lex = boto3.client(
            'lex-runtime',
            region_name=AWSConfig.getRegionName(),
            aws_access_key_id=AWSConfig.getAccessKeyId(),
            aws_secret_access_key=AWSConfig.getSecretKeyId())

    def sendMessage(self, text):
        return self.lex.post_text(
            botName=LexConfig.getBotName(),
            botAlias=LexConfig.getBotAlias(),
            userId=LexConfig.getUserId(),
            inputText=text)
