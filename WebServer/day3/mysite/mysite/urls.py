"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 우리가 만든 app을 정의해야 함.
# 어플리케이션이 추가될 때마다 추가해야 함.
urlpatterns = [
    # defalut로 만들어진 url
    # 127.0.0.1:8000/admin으로 확인 가능
    # admin.site.urls: 실제 패키지를 사용
    path('admin/', admin.site.urls),
    # 첫번째 변수 아무것도 안주면: root
    # 두번째 변수: myapp.urls라는 문자열은 include하라는 뜻
    # 내가 만든 어플리 케이션을 추가시켜주세요~~~
    # myapp아래 urls.py파일을 포함시켜주세용
    # urls.py아래서 사용할 url 라우터 주소를 정의해야 함.
    # 전체적인 application을 추가하고 세부적인 내용은 urls.py에 정의
    path('', include('myapp.urls'))
]
