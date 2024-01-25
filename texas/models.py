# models.py
from django.db import models
from ckeditor.fields import RichTextField

class YourModel(models.Model):
    question = models.TextField()
    content = RichTextField()

class Answer(models.Model):
    question = models.ForeignKey(YourModel, related_name='answers', on_delete=models.CASCADE)
    content = RichTextField()
