from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    # 동적 url 다루기
    # path('<name>/', views.index2),  # 임의의 문자가 다 올 수 있음.
    # path('<int:pk>/detail', views.index3),
    # path('<int:pk>/detail', views.detail, name = 'detail'),


    # 함수 기반
    # path('list/', views.list, name = 'list'),

    # class 기반
    # path('list2/', views.PostView.as_view()),    # as_view()함수를 가지고 PostView 객체 생성
    path('login/', views.LoginView.as_view(), name ='login'),

    # path('add/', views.PostView.as_view(), name = 'add'),
    # path('<int:pk>/edit', views.PostEditView.as_view(), name = 'edit'),

    # 이름: 경로 신경쓰지 말고 name을 경로로 사용할 수 있음.

    # 최종버전
    # 이 뷰가 실행되기 위해서는 파라미터가 2개 있어야 함!
    path('<int:pk>/<mode>', views.PostEditView.as_view(), name = 'edit')
]


# 경로: 
# /붙이면 directory 의미
# /없으면 resorce를 의미
# name을 지정하기 