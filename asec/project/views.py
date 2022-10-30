from django.shortcuts import render
from django.http  import HttpResponse
def index(request):
    return HttpResponse("Hello,world!")
def greeting(request,name):
    return HttpResponse("Hello,{name}!")
# Create your views here.
