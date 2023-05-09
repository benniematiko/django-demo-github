#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_page_views(request):
    return HttpResponse('<h1>Home Page</h1>')
