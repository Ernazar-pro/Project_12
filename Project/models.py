from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['-id']
    
class Posts(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=256, blank=True, null=True)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, verbose_name='author')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Поста'
        verbose_name_plural = 'Посты'

