from django.db import models
# 상속을 받음!
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass