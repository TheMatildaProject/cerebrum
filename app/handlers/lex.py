import boto3, json
from config.aws import AWS as AWSConfig
from config.lex import Lex as LexConfig

class Lex(Object):
    def __init__(Object):
        self.lex = boto3.client(
            'lex-runtime',
            region_name=AWSConfig.getRegionName(),
            aws_access_key_id=AWSConfig.getAccessKeyId(),
            aws_secret_access_key=AWSConfig.getSecretKeyId())

    def sendMessage(Object, text):
        return self.lex.post_text(
            botName=LexConfig.getName(),
            botAlias=LexConfig.getAlias(),
            userId=LexConfig.getUserId(),
            inputText=text)
