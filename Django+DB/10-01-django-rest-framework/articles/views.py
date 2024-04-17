from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from rest_framework import status

# decorator 필수로 써야함!
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
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
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
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
    
@api_view(['GET'])
def comment_list(request):
    # 전체 데이터 조회
    # comments = Comment.objects.all()
    comments = get_list_or_404(Comment)
    # 직렬화
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def comment_detail(request, comment_pk):
#     comments = Comment.objects.get(pk=comment_pk)
#     # 직렬화
#     serializer = CommentSerializer(comments)
#     return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def comment_create(request, article_pk):
    # 게시글 조회
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    # 사용자 입력 데이터를 받아 직렬화 진행
    serializer = CommentSerializer(data=request.data)
    # 유효성 검사 (목록에서 외래키 없애주어야 함)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

