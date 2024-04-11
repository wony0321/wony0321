from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer
from rest_framework import status

# decorator 필수로 써야함!
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        # 이름만 같은 것이지, 다른 것임! DRF의 배려로 이름 같게 해준 것
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 저장 성공한 데이터 알려주고, 응답 상태 알려줌
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패 시에는 데이터 존재 X, 응답 상태 400
        # raise_exception=True 설정하면 아래 코드 생략 가능
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # partial 필수는 아니나, 요청 보낼 때마다 다 보내지 않기 위해 설정
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance=article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)