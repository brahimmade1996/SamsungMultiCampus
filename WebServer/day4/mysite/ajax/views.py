from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.conf import settings
import sys
from io import StringIO


def index(request):
    return HttpResponse('Hello~~~')


def calcForm(request):
    return render(request, 'ajax/calc.html')


# 실제 계산
def calc(request):
    op1 = int(request.GET["op1"])
    op2 = int(request.GET["op2"])
    result = op1 + op2
    # return HttpResponse(f'result = {result}')

    # data를 json형식으로 return하기-> dict이기 때문에 클라이언트가 인식 못함(문자열로 처리)
    # return HttpResponse("{'result':" + str(result) + '}') 

    # dict를 json으로 변환하는 함수 사용
    # jsonResponse: 헤어정보로 json파임임을 명시
    JsonResponse({'error': 0, 'result': result})


def loginForm(request):
    return render(request, 'ajax/login.html')

def login(request):
    id = request.GET["id"]
    pwd = request.GET["pwd"]
    if id == pwd:
        request.session['user'] = id
        return JsonResponse({'error': 0})
    return JsonResponse({'error': -1, 'message': '"id/pwd"를 확인해주세요'})


def dateForm(request):
    return render(request, 'ajax/date.html')

def date(request):
    print(request)
    year = request.GET['year']
    month = request.GET['month']
    day = request.GET['day']
    print(type(year), year)
    return JsonResponse({'year': year, 'month': month, 'day': day})

def uploadForm(request) :
    return render(request, "ajax/upload.html")

def upload(request) :
    file = request.FILES['file1']
    filename = file._name
    fp = open(settings.BASE_DIR + "/static/" + filename, "wb")
    for chunk in file.chunks() :
        fp.write(chunk)
    fp.close()
    return HttpResponse("upload~")


def runpythonForm(request):
    return render(request, 'ajax/runpython.html')


# dict로 지역변수, 전역변수를 저장
glo = {}
loc = {}

def runpython(request) :
    code = request.GET["code"]

    original_stdout = sys.stdout
    sys.stdout = StringIO()
    exec(code, glo, loc)
    contents = sys.stdout.getvalue()
    sys.stdout = original_stdout
    contents = contents.replace("\n", "<br>")

    contents = "<font color=red>result</font><br>" + contents
    return HttpResponse(contents)