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




