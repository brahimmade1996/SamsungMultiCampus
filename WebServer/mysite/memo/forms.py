
from . import models
from django.forms import ValidationError
from django import forms


def validator(value):
    if len(value) < 5 : raise  ValidationError('길이가 너무 짧아요')


class MemoForm(forms.ModelForm):
        # 부가적인 정보를 입력하는 calss
    class Meta:
        # model: 정해진 변수명
        model = models.Memo
        fields = ['title', 'text', 'category']

        # 입력할 때 category, image도 처리해야 함.-> image field는 추가로 처리하기
        
    def __init__(self, *args, **kwargs):
        super(MemoForm, self).__init__(*args, **kwargs)
        self.fields['title'].validator=[validator]
