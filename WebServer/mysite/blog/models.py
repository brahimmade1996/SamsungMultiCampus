from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # 기본키
    # 유저를 지우는 방법
    # 1. # 특정 유저를 지우려면, 모든 것을 지우고 모든 것을 지우거나
    # 2. 유저를 지울 때 글도 같이 지우라는 뜻-> on_delelte= models.CASCADE
    author = models.ForeignKey('auth.User', # 시스템 테이블-> 슈퍼유저 테이블
                            on_delete= models.CASCADE, # 단계별로 진행된다는 뜻
                            )
                                 
    title = models.CharField(max_length = 200)
    text = models.TextField()  # textarea로 받는 부분
    created_data = models.DateTimeField(default =timezone.now)
    published_date = models.DateTimeField(blank = True, # application 관점에서 data가 비어도 되는지
                                            null = True) # 데이터 베이서 관점에서 널값 허용

    # 글을 수정한 날짜
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    # 프린트 함수
    def __str__(self):
        return self.title

