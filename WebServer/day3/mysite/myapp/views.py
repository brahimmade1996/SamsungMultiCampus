from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from face import facerecognition

# 함수명 상관없지만 home이므로 관행적으로 index 사용
# request: 변수명 상관없지만, 관행적으로 request 사용( 브라우저가 전송한 정보를 갖고있는 변수임)
def index(request):
    # 문자열(html) 리턴하기
    # 반드시 HttpResponse 함수 이용해서 출력하기
    return HttpResponse('Hello DJango!!!')


def test(request):
    print(request)

    # 데이터를 dict, list 형으로 보낼 수 있음.
    dict_data = {'img': 'test.png'}
    list_data = [1,2,3,4,5]
    data = {'s': dict_data, 'list': list_data}

    return render(request,  # 전달받은 파라미터
                 'template.html', # 사용할 템플릿 파일
                # {'message': '안녕'} # 플라스크에서는 dict형태로 넘김
                data
                )

# template 안에 login.html이 있는 경우
def login2(request):
    return render(request, 'login2.html')


# static 안에 login.html이 있는 경우
def login(request):
    #request:dict 형태로 클라이언트가 보내주는 정보를 담고 있음.
    id = request.GET.get('id', 0)
    pwd = request.GET.get('pwd',0)
    if id == pwd:
        request.session['user'] = id
        return redirect('/service')

    # return HttpResponse('login fail <a href=static/login.html>다시로그인</a>' )
    return redirect('/static/login.html')


# login 후 나오는 main page
# service main page: 경로명을 알면 바로 접속할 수 있으므로, 인증과정이 필요!
def service(request):
    # 로그인을 하지 않으면 session 값이 없음.
    if request.session.get('user','')=='':
        return redirect('/static/login.html')
    html = 'Main Service <br>' + request.session.get('user') + '님 감사합니다' + '<a href=/loginout> logout</a>'
    return HttpResponse(html)

def loginout(request):
    request.session['user'] ==''
    #request.session.pop('user')
    return redirect('/static/login.html')


@csrf_exempt
def uploadimage(request):
    # file 객체를 이용하여 
    file = request.FILES['file1']
    filename = file._name
     
    # file크기에 따라 chunk에 따라 나눠서 저장 
    # settings.py 파일에 정의된 base dir이 있음.
    fp = open(settings.BASE_DIR + '/static/' + filename, 'wb')
    for chunk in file.chunks():
        fp.write(chunk)
    fp.close()

    html = 'ok:' + '^^' + filename

    model = 'known.bin'
    file ='./static/' + filename 
    # fp.save(file_path)

    result = facerecognition(model, file)
    request.session['user'] = result
    if result !='':
        request.session['user'] = result
        return redirect('/service')
        # html = 'login Sucess <br>' + request.session.get('user') + '님 감사합니다' + '<img src="/static/filename" >'
                                
        # return HttpResponse(html)


    return redirect('/static/login.html')

