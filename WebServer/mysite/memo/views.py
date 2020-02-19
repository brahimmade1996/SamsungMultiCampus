from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import CharField, Textarea, ValidationError
# from django import forms
#from blog.forms import PostForm  # 프로젝트 명이 바뀌면 blog를 바꿔야하므로 좋지 않음
from . import models
from . import forms
from . import apps

# url: bolg -> index함수 실행
def index(request):
    return HttpResponse('ok')

### <int:pk>/ <mode>를 url을 사용하기 위해
class MemoView(View) :
    def get(self, request,category, pk, mode):
        print(pk, mode)
        if mode =='add':
            form = forms.MemoForm()
            return render(request, apps.APP +'/edit.html', {'form': form})
        
        elif mode == 'list':
            username = request.session.get('username', '')
            user = User.objects.get(username =username)
            data= models.Memo.objects.all().filter(author = user)
            context = {'data': data,'username': username, 'category': category}
            return render (request, apps.APP + '/list.html', context)

        elif mode =='detail':
            p = get_object_or_404(models.Memo, pk = pk)
            # 조회수 증가
            p.cnt +=1
            p.save()
            return render(request, apps.APP + '/detail.html', {'d': p, 'category': category})

        elif mode == 'edit':
            post = get_object_or_404(models.Memo, pk=pk)
            form = forms.MemoForm(instance=post)

    
        else:
            return HttpResponse('mode를 잘 입력하세용')
        return render(request, apps.APP + "/edit.html", {"form":form})



    def post(self, request,category, pk, mode):

        username = request.session["username"]
        user = User.objects.get(username=username)

        if pk == 0:
            form = forms.MemoForm(request.POST)
        else:
            post = get_object_or_404(models.Memo, pk=pk)
            form = forms.MemoForm(request.POST, instance=post)
            print(post, form)

        if form.is_valid():
            post = form.save(commit=False)
            # add할 때 저자정보 넣고
            if pk == 0:
                post.author = user
            post.save()
            # urls.py의 name을 써야 함!!!!!!!!!1
            return redirect("Memo", category, 0, 'list')  
        return render(request, apps.APP + "/edit.html", {"form": form})
            
          


