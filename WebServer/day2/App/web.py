from flask import Flask, render_template, request
import yolo
import cv2

app = Flask(__name__)

# 글로벌 변수처럼 생성
listData=[{'id':'0','img':'img1.jpg', 'title': 'candy'},
            {'id':'1','img':'img2.jpg', 'title': 'chocolate'},
            {'id':'2','img':'img3.jpg', 'title': 'donut'}]

@app.route('/')
def index():
    return render_template('home.html', title = 'my home page')


@app.route('/image')
def image():
    # render-template(참고할 html문서, html문서 변수명 = py파일의 변수명)
    return render_template('image.html', listData = listData) 

# /view?id=id로 실행
@app.route('/view')
def view():
    # get 방식
    id =request.args.get('id')
    return render_template('view.html', s = listData[int(id)]) 

def goURL(msg, url):
    html = '''
            <script>
                alert("@msg");
                window.location.href = '@url';
            </script>
            '''
    html = html.replace('@msg', msg)
    html = html.replace('@url', url)
    return html


@app.route('/fileUpload', methods = ['POST'])
def fileUpload():
    if request.method=='POST':
        f = request.files['file1']
        # post 방식
        # 물리적인 폴더 경로 입력
        file_path ='./static/' + f.filename 
        f.save(file_path)


        title = request.form.get('title')
        # id = len(Data)
        id = int(listData[len(listData)-1]['id']) + 1
        listData.append({'id': len(listData), 'img': f.filename,'title': title})


        yolo_image =yolo.detectionObject(file_path)
        filename = f.filename.replace('.jpg','')
        yolo_file_path = f'./static/{filename}_yolo.jpg'
        yolo_img_name = f'{filename}_yolo.jpg'
        cv2.imwrite(yolo_file_path, yolo_image) 

        listData.append({'id': len(listData), 'img': yolo_img_name,'title': title})
        # print(listData)

        # 새창에 이미지 보여줄 때
        # return f'파일 "{title}" 업로드 성공 <br><img src={yolo_file_path}>'
        return render_template('image.html', listData = listData) 


@app.route('/deleteImage') # delete?id = 0
def deleteImage():
    idx = -1
    id =int(request.args.get('id'))
    for i in range(len(listData)):
        if id == listData[i]['id']:
            idx = i
        if idx >= 0: del listData[idx]
    return goURL('이미지가 삭제되었습니다', '/image')



if __name__ =='__main__':
    app.run(host ='0.0.0.0', port = 100, debug=True)