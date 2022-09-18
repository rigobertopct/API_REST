from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(verbose_name='titulo', max_length=255)
    content=models.TextField(verbose_name='contenido', default='xxxx')