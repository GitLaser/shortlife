# -*-coding:utf8 -*-
from django.urls import path

__author__ = "陈子昂"
__datetime__ = "2018/1/20 17:29"

from . import views

urlpatterns = [
path('add_book', views.add_book, ),
path('show_book/<book_id>/', views.ShowBook.as_view(),name='show_book' ),
]
