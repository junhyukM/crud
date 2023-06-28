# Model

- 'models.py'
```python
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
```

- 번역본 생성
    - python manage.py makemigrations

- DB에 반영
    - python manage.py migrate

- SQL 스키마 확인
    - python manage.py sqlmigrate posts 0001

- admin.py 수정 
```python
from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)
```




