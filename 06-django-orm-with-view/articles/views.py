from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # 여기서 pk는 전혀 관계없는 것이긴하지만 표현을 pk=pk라고 함
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/details.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # print(request.GET)
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 유효성 검증 가능 but 복잡
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 유효성 검증을 위해 2번 택함
    article = Article(title=title, content=content)
    article.save()

    # 구조상 유효성 검증할 수 없어서 3번째 방법은 택하지 않음
    # Article.objects.create(title=title, content=content)    
    # return render(request, 'articles/create.html')

    # return redirect('주소', 파라미터)
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 몇 번 글 삭제할건데? -> 조회
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 몇 번 게시글 수정? -> 조회 필요
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    # 새로운 인스턴스 만들어버리면 안됨 so 수정은 기존 값을 바꾸어야 함
    # article = Article(title=title, content=content)
    # article.save()
    article.title = title
    article.content = content
    article.save()

    # return redirect('주소', 파라미터)
    return redirect('articles:detail', article.pk)

