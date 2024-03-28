from django import forms

# 모델폼을 만들어라 -> 사용해야 하는 Model class를 Improt 해야함
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = '__all__'