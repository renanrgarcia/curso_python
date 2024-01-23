from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.


def blog(request):
    print('blog')
    return HttpResponse('blog do app 1')


def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo do app 1')
