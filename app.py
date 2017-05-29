import os, sys
from flask import Flask, jsonify, request
from app.handlers.lex import Lex as LexHandler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def app():
    if not request.json or not 'message' in request.json:
        return jsonify({'message': 'Missing message'}), 400
    
    response = LexHandler.sendMessage(request.json['message'])

    return jsonify({'response': response});

if __name__ == "__main__":
    app.run(debug=True)