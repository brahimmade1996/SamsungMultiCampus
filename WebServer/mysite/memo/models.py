from django.db import models
from django.utils import timezone

# Create your models here.
class Memo(models.Model):
    
    author = models.ForeignKey('auth.User',
                            on_delete= models.CASCADE, 
                            )
                                 
    title = models.CharField(max_length = 200)
    text = models.TextField()  # textarea로 받는 부분
    created_data = models.DateTimeField(default =timezone.now)
    published_date = models.DateTimeField(blank = True, # application 관점에서 data가 비어도 되는지
                                            null = True) # 데이터 베이서 관점에서 널값 허용

    cnt = models.IntegerField(default = 0)
    image = models.CharField(max_length=200, null = True, blank = True)


    # QnA인지 게시판 별 구분할 수 있는 filed
    category = models.CharField(max_length = 10, default = 'common')
    
    # 프린트 함수
    def __str__(self):
        return self.title

