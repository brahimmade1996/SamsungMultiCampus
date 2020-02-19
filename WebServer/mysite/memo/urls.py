from django.urls import path
from . import views 
from django.shortcuts import redirect

urlpatterns = [
    path('', views.index),
    path('<category>/<int:pk>/<mode>', views.MemoView.as_view(), name = 'Memo'),
    path('', lambda request: redirect('memo', 'common', 0, 'list')),
]
