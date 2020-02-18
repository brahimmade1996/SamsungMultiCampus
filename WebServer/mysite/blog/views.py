from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate
from django.forms import Form
from django.forms import CharField, Textarea,  ValidationError



# Create your views here.

# url: bolg -> index함수 실행
def index(request):
    return HttpResponse('ok')

# 동적 url 
# name이라는 파라미터를 usr주소에 사용
# url: blog/abe -> index2함수 호출
# def index2(request, name):
#     return HttpResponse('ok'+name)

# def index3(request, pk):
#     # pk: table에서 직접적을 field명을 알 수 없음(실제로는 id임)
#     # pk: pk = 1인 값을 찾아야 함.
#     # p = Post.objects.get(pk = pk)

#     # 예외처리
#     p = get_object_or_404(Post, pk = pk) # errer를 return하고 종류
#     return HttpResponse('ok' + p.title)


def list(request):
    # 모든 글 보여주기
    # data =Post.objects.all()

    # user가 쓴 글만 갖고오기
    username = request.session.get('username', '')
    user = User.objects.get(username =username)
    data= Post.objects.all().filter(author = user)
    context = {'data': data,'username': username}
    return render (request,'blog/list.html', context)

def detail(request, pk):
    p = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/detail.html', {'d': p})



# View를 상속받아서 정의
# get, post 나눠서 정의
# 특정 url이 호출되면 PoseView instance가 생성
class PostView(View):
        
    def get(self, request):
        return render(request, 'blog/edit.html')
    def post(self, request):

        title = request.POST.get('title')
        text = request.POST.get('text')
        username = request.session['username']
        user = User.objects.get(username = username)

        Post.objects.create(title = title, text=text, author = user)

        return HttpResponse('post ok')



# 이 구조에서는 항상 get 방식은 render해야 함-> form을 띄워야 함.
# 이 구조에서는 항상 get 방식은 redirect해야 함-> form을 처리한 후, 다른 url로 연결

class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):

        # user table의 password는 암호화되어 들어가있음.-> 간접적으로 비교 해야 함.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 장고에서 지원하는 함수
        user = authenticate(username =username, password = password)
        if user == None:
            return redirect('login')

        request.session['username'] = username

        return redirect('list')


def validator(value):
    if len(value) < 5 : raise  ValidationError('길이가 너무 짧아요')

class PostForm(Form):
    title = CharField(label = '제목', max_length = 20, validators=[validator])
    text = CharField(label = '내용', widget = Textarea) # widget: ui를 의미



# 특정 post를 수정해야 함 -> 파라미터를 받아야 함(pk= id)
class PostEditView(View):
    def get(self, request, pk):

        # # 데이터에 초기값 지정
        # post = Post.objects.get(pk = pk)
        # # 모든 변수를 모두 매핑하면 복잡해지므로
        # # Form data를 사용하기
        # form = PostForm()
        post = get_object_or_404(Post, pk = pk)
        form = PostForm(initial = {'title': post.title, 'text': post.text})
        return render(request, 'blog/edit.html', {'form': form ,'pk':pk})

    def post(self, request, pk):
        # create가 아님
        # 이미 만들어진 객체를 갖고오기
        # 만든 객체를 rendering
        
        form = PostForm(request.POST)
        # validator를 통화하면 처리
        if form.is_valid():
            post = get_object_or_404(Post, pk = pk)
            post.title = form['title'].value()
            post.text = form['text'].value()
            post.publish()

            return redirect('list')
        return render(request, 'blog/edit.html', {'form': form ,'pk':pk})