from flask import Flask, request, jsonify
import requests
import json
import urllib
from bs4 import BeautifulSoup

app=Flask(__name__)



def getWeather(city):
    url = 'https://search.naver.com/search.naver?query='
    url = url + urllib.parse.quote_plus(city + '날씨')
    print(url)
    bs = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    temp = bs.select('span.todaytemp')
    desc = bs.select('p.cast_txt')
    return {'temp':temp[0].text, 'desc':desc[0].text}

@app.route('/weather')
def weather():
    city = request.args.get('city')
    info = getWeather(city)
    # return '<font color=red>'+info['temp']+'도  ' + info['desc'] +'>/font>' # 출력은 무조건 문자열
    # return json.dumps(info)
    return jsonify(info)

@app.route('/dialogflow', methods = ['POST', 'GET'])
def dialogflow():
    res = {'fulfillmentText': 'Hello'}
    return jsonify(res)






@app.route('/')
def home():
    # name: 브라우저에서 호출하면 그 valud값을 불러옴.
    name = request.args.get('name')
    item = request.args.get('item')
    return 'hello~~' + name + item







@app.route('/abc')
def home2():
    return 'abc hello~~'


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 4000, debug = True)