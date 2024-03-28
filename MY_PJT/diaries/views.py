from django.shortcuts import render, redirect
from .models import Diary
from .forms import DiaryForm

# Create your views here.

def index(request):
    # 모든 diary 정보를 사용자에게 보여줘야 함
    diary_list = Diary.objects.all()
    context = {
        'diary_list': diary_list
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        # POST 일 때는 DB에 저장하는 로직
        # 사용자의 입력값을 넣자!
        form = DiaryForm(request.POST, request.FILES)  # 사용자의 입력값을 넣자

        if form.is_valid(): # 저장해도 되는 data인지 확인
            form.save()     # DB에 저장
            # 방금 작성한 페이지로 갈 것인지?(detail 기능이 추가되면)
            # 전체 목록으로 갈 것인지를 정하면 됨
            # diary_list = Diary.objects.all()
            # context = {
            #     'diary_list': diary_list
            # }                                 # 반복되는 코드(index와 겹침 -> index가 할 수 있는 일임!)
            return redirect('diaries:index')
        # DB에 저장하고 나서 index 페이지를 보여줄 것임
    else:
        # 사용자가 입력할 수 있는 create.html 페이지를 보여줄 것임
        form = DiaryForm()   # 사용자가 생성하는 부분이라 인자를 넣지 않아야 함
        # form을 이제 create.html에서 보여주자!
    context = {
        'form': form,
    }
    return render(request, 'diaries/create.html', context)
