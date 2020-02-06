from flask import Flask, request, jsonify
import requests
import json
import urllib
from bs4 import BeautifulSoup

app=Flask(__name__)


@app.route('/')
def home():
    html = '''
    <h1> Hello </H1>
    <img src=/static/cake.jpg></img>
    <br>
    <iframe 
        height="430" width="350" 
        src="https://bot.dialogflow.com/SMChatBot-shiney0001">
    </iframe>
    '''
    return html

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 4000, debug = True)