from flask import Flask, escape, request,g
import pprint
import urllib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'

# app이 만들어짐
app = Flask(__name__)

id = 0
db ={'0': {'email': 'john@johnsmith.com',
       'id': 0,
       'image_url': 'http://dn-m.talk.kakao.com/talkm/bl3wxRnVo6e/6XiB4ND7TkYT7TaDpPaGkK/i_uxe4voeqeyg3.png',
       'name': 'JOHNSMITH',
       'phone': '+1 077 7853265'}}


# 명함 인식
@app.route('/namecard', methods = ['POST'])
def namecard():
    global id
    body = request.json
    # pprint.pprint(body)
    image_url = body['userRequest']['params']['media']['url']
    print(image_url)
    img_file = './image.jpeg'
    if image_url.startswith('http://dn-m.talk.kakao.com/'):
        urllib.request.urlretrieve(image_url, img_file)

        # with urllib.request.urlopen(image_url) as input:
        #     with open('./image.jpeg', 'wb') as output:
        #         output.write(input.read())
    

    info = ocr(img_file)

    db_value = creat_namecard(info, image_url)
    # print('db_value', db_value)
    id= id + 1
    db_value['id']=id
    db[str(id)]= db_value
    pprint.pprint(db)
    return db, image_url

def creat_namecard(info, image_url):
    db_value = {'email': '이메일 없음',
       'id': 0,
       'image_url': 'http://dn-m.talk.kakao.com/talkm/bl3wxRnVo6e/6XiB4ND7TkYT7TaDpPaGkK/i_uxe4voeqeyg3.png',
       'name': '이름 없음.',
       'phone': '010-1234-578'}
    db_value['image_url'] = image_url
    card_text = info.split('\n\n')   #.replace('-', '')
    # print('card_text', card_text)

    for i, text in enumerate(card_text):
        
        text = text.replace('-','')
        print(i, text)

        if len(text)>=2:
            sub_text =text.split('\n') 
            # print('sub_text', sub_text)
            for j, sub_sub_text in enumerate(sub_text):
                # name저장
                a = not sub_sub_text.isdigit() 
                b = len(sub_sub_text.split(' '))==1
                c = len(sub_sub_text.split('@'))==1
                d = len(sub_sub_text.split('.'))==1

                if a and b and c and d:
                    db_value['name']= sub_sub_text
                # email저장
                if '@' in sub_sub_text:
                    db_value['email'] = sub_sub_text
                # url저장
                if sub_sub_text.startswith('www'):
                    db_value['url'] = sub_sub_text
                # phone 저장
                if sub_sub_text.isdigit() or sub_sub_text.startswith('+'):
                    db_value['phone']= sub_sub_text
                    continue
    print('creat_namecard', creat_namecard)
    return db_value


def ocr(img_file):
    image = cv2.imread(img_file, 1)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,gray2 = cv2.threshold(gray,180,255,cv2.THRESH_BINARY)
    gray = cv2.medianBlur(gray2, 5)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cnts, z = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    approx_con=[]

    for con in cnts:
        peri = cv2.arcLength(con,True)#폐곡선 컨투어 길이
        approx = cv2.approxPolyDP(con,peri*0.02,True)#
        approx_con.append(approx)
    approx_con = np.array(approx_con)
    point_list = approx_con[0].reshape(4,2)
    height,width=image.shape[:2]

    pts1 = np.float32([list(point_list[0]),
                    list(point_list[1]),
                    list(point_list[2]),
                    list(point_list[3])])


    if pts1[1][1] < pts1[0][1]:
        pts1[0,1] = pts1[1,0]
    if pts1[2][1] < pts1[3][1]:
        pts1[2,3] = pts1[3,2]
        
        

    pts2 = np.float32([[0,0],
                    [0,height],
                    [width,height],
                    [width,0]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    right_image = cv2.warpPerspective(image,M,(width,height))
    str = pytesseract.image_to_string(right_image,lang='eng+kor')

    return str


# GET: 조회
@app.route('/namecard_search', methods = ['POST'])
def select_user():
    # return db[str(id)]
    body = request.json
    id = body['action']['detailParams']['id']['origin']
    
    # print('dbid',db[str(id)])

    while id not in db.keys():
        body = request.json
        id = body['action']['detailParams']['id']['origin']
        return{
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "다시 id를 입력하세요."
                    }
                }
            ]
        }
    }

    return {
        "version": "2.0",
        "template": {
            "outputs": [
            {
                "basicCard": {
                "title": db[str(id)]['name'],
                "description": "불금 콜?!",
                "thumbnail": {
                    "imageUrl": db[str(id)]['image_url']
                },
                "profile": {
                    "imageUrl": db[str(id)]['image_url'],
                    "nickname": "보물상자"
                },
                "social": {
                    "like": 1238,
                    "comment": 8,
                    "share": 780
                },
                "buttons": [
                    {
                    "action": "phone",
                    "label": "call",
                    "phoneNumber": db[str(id)]['phone']
                    },
                    {
                    "action":  "webLink",
                    "label": "E-mail",
                    "webLinkUrl":db[str(id)]['email']
                    }
                ]
                }
            }
            ]
        }
        }
    # else:
    #     return{
    #     "version": "2.0",
    #     "template": {
    #         "outputs": [
    #             {
    #                 "simpleText": {
    #                     "text": "다시 id를 입력하세요."
    #                 }
    #             }
    #         ]
    #     }
    # }
   

    
    