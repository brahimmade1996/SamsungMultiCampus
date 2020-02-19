from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import CharField, Textarea, ValidationError
from django import forms
#from blog.forms import PostForm  # 프로젝트 명이 바뀌면 blog를 바꿔야하므로 좋지 않음
from . import models
from . import forms
from . import apps

# url: bolg -> index함수 실행
def index(request):
    return HttpResponse('ok')

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
            context = {'data': data,'username': username, 'category': category}
            return render (request, apps.APP + '/list.html', context)

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
            
          


