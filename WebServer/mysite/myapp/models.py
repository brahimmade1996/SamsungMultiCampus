from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    userid = models.CharField(max_length = 10, primary_key = True)
    name = models.CharField(max_length= 10)
    age = models.IntegerField()
    hobby = models.CharField(max_length = 20)

    # 시스템함수
    # print()할 때 자동으로 출력됨.
    # user를 입력하고 save하면 보여지는 page에 출력됨.
    def __str__(self):
        # return self.userid + '/' + self.name + '/' + self.age
        return f"{self.userid} / {self.name}/ {self.age}"
        
