from django.db import models

def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 빈 문자열로도 저장될 수 있도록 True 설정
    # 아니면 모든 게시글에 이미지 넣어야 함
    image = models.ImageField(blank=True, upload_to='uploaded_files')
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # image = models.ImageField(blank=True, upload_to=articles_image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
