from flask import Flask, escape, request

# app이 만들어짐
app = Flask(__name__)


# REST의 url부분: 도메인이 빠진 하위 부분을 코딩
# 리턴하는 값이 응답
@app.route('/')
def hello():
    name = request.args.get('name', 'world')
    return f'Hello, {escape(name)}!'

# json으로 return
@app.route('/hi',methods=['GET', 'POST'])
def hi():
    return{
        'version': '2.0',
        'templete': {
            'outputs': [
                {
                    'simpleText': {
                        'text': '간단한 텍스트 요소입니다'
                    }
                }
            ]
        }
    }    

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
#     app.run()