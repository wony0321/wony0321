from django.db import models


# Create your models here.
# 1쪽
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# N쪽
class Comment(models.Model):
    # 단수형으로 받아옴
    # on_delete는 게시글이 지워지면 댓글도 다 지우는 기능
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)