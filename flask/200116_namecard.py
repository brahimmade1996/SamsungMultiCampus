from flask import Flask, escape, request
import pprint
import urllib
import cv2
import numpy as np
import matplotlib.pyplot as plt
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
    if image_url.startswith('http://dn-m.talk.kakao.com/'):
        urllib.request.urlretrieve(image_url, './image.jpeg')

        # with urllib.request.urlopen(image_url) as input:
        #     with open('./image.jpeg', 'wb') as output:
        #         output.write(input.read())
    

    info = ocr('./image.jpeg')
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

    
def ocr(file):
    img = cv2.imread(str(file), 1)
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
        if len(approx) == 4:
            cv2.drawContours(pic, [approx], -1, (0, 255, 0), 4)

    height, width = img.shape[:2]
    # 좌표 순서 = 왼쪽 상단끝, 상단 오른쪽 끝, 하단 왼쪽 끝, 하단 오른쪽끝
    point_list = approx_con[0].reshape(4,2)
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







# if __name__ == '__main__':
#     info = ocr(default ='./image.jpeg')
#     print('=====')
#     print(info)
