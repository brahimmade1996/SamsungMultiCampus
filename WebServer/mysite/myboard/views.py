from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import CharField, Textarea, ValidationError
from django import forms
#from blog.forms import PostForm  # 프로젝트 명이 바뀌면 blog를 바꿔야하므로 좋지 않음
from . import models
from . import forms
from . import apps
from django.core.paginator import Paginator

# url: bolg -> index함수 실행
def index(request):
    return HttpResponse('ok')

# get방식으로 하기
# 지워달라는 요청, 특정 데이터를 요청할 수 있음
def ajaxdel(request):
    pk = request.GET.get('pk')
    board = models.Board.objects.all().get(pk = pk)
    # db에서 지우기
    # board.delete()  # 연습할 때는 진짜 db가 지워지지 않도록 주석처리하기
    return JsonResponse({'error': '0'})


# 특정 페이지의 모든 데이터 
def ajaxget(request):
    page = request.GET.get('page', 1)
    datas = models.Board.objects.all().filter(category = 'common')  # data가 없으면 queryset은 None을 return
    print(datas)
    # page개념이 아니므로 슬라이싱으로 해도 상관없음.-> len==0일 때 경고 나오게 하려면 슬라이싱으로 해야 함.
    page = int(page)
    subs = datas[(page-1)*3: (page*3)]
    # p = Paginator(datas, 3)
    # subs = p.page(page)

    datas = {'datas': [{'pk': data.pk, 'title': data.title, 'cnt': data.cnt} for data in subs]}
    return JsonResponse(datas, json_dumps_params = {'ensure_ascii': False})  # 한글 오류 -> utf-8로 인코딩됨



def page(request):
    datas = [{'id': 1, 'name':  '홍길동1'},
            {'id': 2, 'name':  '홍길동2'},
            {'id': 3, 'name':  '홍길동3'},
            {'id': 4, 'name':  '홍길동4'},
            {'id': 5, 'name':  '홍길동5'},
            {'id': 6, 'name':  '홍길동6'},
            {'id': 7, 'name':  '홍길동7'},
            ]

    page = request.GET.get('page', 1)  #default: 1
    p = Paginator(datas, 3)# collections 형태의 데이터,  # 한 페이지에 보여줄 데이터 개수
    sub = p.page(page) # 몇번째 페이지를 가지고 올 지 
                    # 슬라이싱의 개념과 같음

    return render(request, 'myboard/page.html', {'datas': sub})


### <int:pk>/ <mode>를 url을 사용하기 위해
class BoardView(View) :
    def get(self, request, category, pk, mode):
        print(pk, mode)
        if mode =='add':
            # pk값은 상관없음.
            form = forms.BoardForm()
            return render(request, 'myboard/edit.html', {'form': form})
        elif mode == 'list':
            # pk값 상관없음.
            username = request.session.get('username', '')
            user = User.objects.get(username =username)
            data= models.Board.objects.all().filter(author = user, category = category)
            
            # page 개념
            page = request.GET.get('page', 1)  
            p = Paginator(data, 3)
            subs = p.page(page) 
            
            context = {'datas': subs,'username': username, 'category': category}
            return render (request, apps.APP + '/pagelist.html', context)

        elif mode =='detail':
            p = get_object_or_404(models.Board, pk = pk)
            # 조회수 증가
            p.cnt +=1
            p.save()
            return render(request,  apps.APP + '/detail.html', {'d': p, 'category': category})

        elif mode == 'edit':
            post = get_object_or_404(models.Board, pk=pk)
            form = forms.BoardForm(instance=post)

        elif mode =='delete':
            post = get_object_or_404(models.Board, pk=pk)
            post.delete()
            return redirect(category +'/0/list')
        else:
            return HttpResponse('mode를 잘 입력하세용')
        return render(request, apps.APP +'/edit.html', {"form":form}) # 정확하게 입력



    def post(self, request, category, pk, mode):

        username = request.session["username"]
        user = User.objects.get(username=username)

        if pk == 0:
            form = forms.BoardForm(request.POST)
        else:
            # 바뀌기 전 데이터
            post = get_object_or_404(models.Board, pk=pk)
            # 바뀌기 전 데이터로부터 form을 생성
            form = forms.BoardForm(request.POST, instance=post)

        if form.is_valid():
            # 바뀐 데이터를 저장은 하지 말고 post에 갖고 오기
            post = form.save(commit=False)
            # add할 때 저자정보 넣고
            if pk == 0:
                post.author = user
                post.category = category
            post.save()
            return redirect("myboard", category, 0, 'list')  
        # return render(request, "myboard/edit.html", {"form": form})
        return render(request, apps.APP + '/edit.html', {"form": form})
            
          


