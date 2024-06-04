from django.db import models

# Create your models here.
class Post(models.Model) :
    # title, content, author, createdAt, updatedAt
    title = models.CharField(max_length = 40)
    content = models.TextField(null = True, blank = True)
    author = models.CharField(max_length = 20)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)