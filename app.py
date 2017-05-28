import boto3

lex = boto3.client('lex-runtime', region_name='us-east-1', aws_access_key_id='', aws_secret_access_key='')

response = lex.post_text(botName='Matilda', botAlias='matilda', userId='matilda', inputText='Hi!')
print(response)