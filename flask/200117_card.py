from flask import Flask, escape, request
import pprint
import urllib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'


def imshow(tit, image):
    plt.title(tit)
    if len(image.shape) == 3:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(image, cmap = 'gray')
    plt.show()

# app이 만들어짐
app = Flask(__name__)


# 명함 인식
@app.route('/namecard', methods = ['POST'])
def namecard():
    body = request.json
    pprint.pprint(body)
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
    card_text, db =json_save(img_file)
    # print('card_text', card_text)
    # print('db', db)
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": info
                    }
                }
            ]
        }
    }    
@app.route('/users', methods = ['POST'])
def creat_namecard(img_file):
    db = {}
    info= ocr(img_file)
    print('info', info)
    card_text = info.split('\n\n')   #.replace('-', '')
    print('card_text', card_text)

    for i, text in enumerate(card_text):
        text = text.replace('-','')
        print(i, text)

        if len(text)>=2:
            sub_text =text.split('\n') 
            print('sub_text', sub_text)
            for j, sub_sub_text in enumerate(sub_text):
                # name저장
                a = not sub_sub_text.isdigit() 
                b = len(sub_sub_text.split(' '))==1
                c = len(sub_sub_text.split('@'))==1
                d = len(sub_sub_text.split('.'))==1

                if a and b and c and d:
                    db['name']= sub_sub_text
                # email저장
                if '@' in sub_sub_text:
                    db['email'] = sub_sub_text
                # phone 저장
                if sub_sub_text.isdigit() or sub_sub_text.startswith('+'):
                    db['phone']= sub_sub_text
                    continue
    print('db', db)
    return card_text, db




def ocr(img_file):
    img = cv2.imread(str(img_file), 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    height, width = img.shape[:2]
    pic =img.copy()
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area_con =[] 
    approx_con = []
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        area = cv2.contourArea(contour)
        area_con.append(area)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        approx_con.append(approx)
        # if len(approx) == 4:
        #     cv2.drawContours(pic, [approx], -1, (0, 255, 0), 4)

    height, width = img.shape[:2]
    # 좌표 순서 = 왼쪽 상단끝, 상단 오른쪽 끝, 하단 왼쪽 끝, 하단 오른쪽끝
    # print(approx_con, approx_con.shape)
    point_list = np.array(approx_con[0]).reshape(4,2)
    pts1 = np.float32([list(point_list[1]),
                  list(point_list[0]),
                  list(point_list[2]),
                  list(point_list[3])])

    pts2 = np.float32([[0,0],[width/2,0],[0,height/2],[width/2, height/2]])
              
    M = cv2.getPerspectiveTransform(pts1, pts2)
    img_result = cv2.warpPerspective(img, M, (int(width/2), int(height/2)))

    # imshow('', img_result)
    cv2.imwrite('./imgs/namecard1.png', img_result)
    ocr_text =pytesseract.image_to_string('./imgs/namecard1.png')

    return ocr_text



    
    


# dictionary를 db처럼 사용하면서 REST 개념 익히기
db = {
    "0":{
        "name": "bill",
        "phone": "010-1234-4567"
    }
}
id = 0

# CREATE: 생성
# post
@app.route('/users', methods = ['POST'])
def create_user():
    global id
    body = request.get_json()
    print('body', type(body), body)
    body['id']= id
    db[str(id)] = body
    id += 1
    # print(db)
    return body 

# GET: 조회
@app.route('/users/<id>', methods = ['GET'])
def select_user(id):
    return db[str(id)]

# DELETE
@app.route('/users/<id>', methods = ['DELETE'])
def delete_user(id):
    del db[str(id)]
    return db

# UPDATE
@app.route('/users/<id>', methods = ['PUT'])
def update_user(id):
    body = request.get_json()
    if id in db.keys():
        db[str(id)].update(body)
    else:
        db[str(id)]= body
    return db







# if __name__ == '__main__':
#     info = ocr(default ='./image.jpeg')
#     print('=====')
#     print(info)
