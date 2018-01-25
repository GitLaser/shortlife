import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from django.views.decorators.http import require_http_methods

from book.models import Book


@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book_name = request.GET.get('book_name','')
        book = Book(name=book_name)
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


class ShowBook(View):
    def get(self,request,book_id):
        print(book_id)
        book = Book.objects.get(pk=book_id)
        return render(request,'showbook.html',{'id':book_id,'name':book.name})