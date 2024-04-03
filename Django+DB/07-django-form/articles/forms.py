from django import forms
from .models import Article

# forms라는 모듈에 form 상속
# 모델하고 유사
# form은 데이터를 DB에 저장하지 않고 그냥 로그인 등 할때 사용
# DB에 저장해야할 때에는 ModelForm 사용함
# class ArticleForm(forms.Form):
#     # texttype input을 만들어내는 것
#     title = forms.CharField(max_length=10)
#     # Textfield 존재하지 않아서 그냥 다 CharField
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    # widget -> meta 태그 위에 작성하는걸 권장
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )

    title = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    # 메타 클라스 작성
    # 이렇게만 작성해도 Textarea로 설정해쥼
    class Meta:
        # 어떤 모델과 연동할 것인지 적는 변수 (호출해서는 안됨)
        model = Article
        # 연동된 모델과 어떤 필드를 쓸지?
        # fields = ('title', 'content') 이렇게 말고
        fields = '__all__'
        # exclude = ('title',)
        