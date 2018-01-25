# -*-coding:utf8-*-
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50,verbose_name="书名")
    add_time = models.DateTimeField(auto_now_add=True,verbose_name="添加时间")

    def __str__(self):
        return self.name