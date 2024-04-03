from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # '__all__'은 입력 데이터가 필요한 모든 필드 출력
        # fields = '__all__'
        fields = ('content',)