
from django.urls import path
from . import views  # current 폴더에 있는 views.py import

# 우리가 만든 app을 정의해야 함.
# 어플리케이션이 추가될 때마다 추가해야 함.
urlpatterns = [
    # root url이 요청되면 
    # current 폴더에 있는 view.py 파일에 있는 index 함수를 실행하기
    path('', views.index),
    path('test', views.test),
    path('login2', views.login2),
    path('login', views.login),
    path('service', views.service),
    path('loginout', views.loginout),
    path('uploadimage', views.uploadimage),

]
