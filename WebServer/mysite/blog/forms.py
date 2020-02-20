
from . import models
from django.forms import ValidationError
from django import forms


def validator(value):
    if len(value) < 5 : raise  ValidationError('길이가 너무 짧아요')


class PostForm(forms.ModelForm):
        # 부가적인 정보를 입력하는 calss
    class Meta:
        # model: 정해진 변수명
        model = models.Post
        fields = ['title', 'text']
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].validator=[validator]
