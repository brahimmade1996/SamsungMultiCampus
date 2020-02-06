from flask import Flask, request, jsonify
import requests
import json
import urllib
from bs4 import BeautifulSoup

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 한글 출력 



# 전역변수
cnt = 0

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



@app.route('/conuter') # 라우터
def counter():
    global cnt
    cnt += 1
    html = "".join([f'<img src=/static/{i}.png width=32' for i in str(cnt)])
    html +='명이 방문하였습니다'    
    return html


@app.route('/weather', methods = ['POST', 'GET'])
def weather():
    # req = request.args if request.method == 'GET' else request.form
    if request.method == 'POST':
        # dict.git
        req = request.args
    else:
        req = request.form
    city = req.get('city')
    
    return f"{city}날씨 좋아요"

def getQuery(word) :
    url = "https://search.naver.com/search.naver?where=kdic&query="
    url = url + urllib.parse.quote_plus(word)
    print(url)
    bs = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    output = bs.select('p.txt_box')
    
    return [node.text for node  in output ]
    #return output[0].text

def getWeather(city) :    
    url = "https://search.naver.com/search.naver?query="
    url = url + urllib.parse.quote_plus(city + "날씨")
    print(url)
    bs = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    temp = bs.select('span.todaytemp')    
    desc = bs.select('p.cast_txt')    
    return  {"temp":temp[0].text, "desc":desc[0].text} 


def processDialog(req) :
    
    answer = req['queryResult']['fulfillmentText']
    intentName = req['queryResult']['intent']['displayName'] 
    
    if intentName == 'query' :
        word = req["queryResult"]['parameters']['any'] 
        text = getQuery(word)[0]                
        res = {'fulfillmentText': text}   
    elif  intentName == 'order_food,num' :
        price = {"짜장면":5000, "짬뽕":10000, "탕수육":20000}
        params = req['queryResult']['parameters']['food_number']
        output = [ food.get("number-integer", 1)*price[food["food"]]  for food in params ]
        text_price = sum(output) 
        print(text_price)
        res = {'fulfillmentText': text_price}
        
    elif intentName == 'weather' :        
        date = req['queryResult']['parameters']['date']
        geo_city = req['queryResult']['parameters']['geo-city']                    
            
        info = getWeather(geo_city)            
        text = f"{geo_city} 날씨 정보 : {info['temp']} /  {info['desc']}"
        res = {'fulfillmentText': text}

    else:
        res = {'fulfillmentText': answer}          
        
    return res


@app.route('/dialogflow', methods = ['POST', 'GET'])
def dialogflow():

    if request.method == 'GET':
        file = request.args.get('file')
        with open(file, encoding = 'UTF8') as json_file:
            req = json.load(json_file)
            print(json.dumps(req, indent = 4, ensure_ascii=False))
    else:
        req = request.get_json(force = True)
        print(json.dumps(req, indent= 4, ensure_ascii=False))
        # res = jsonify(processDialog(req))
    return jsonify(processDialog(req))

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 4000, debug = True)