from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def add(request):
    return HttpResponse('<marquee><h1>addition using + to add two numbers</h1></marquee>')

def sub(request):
    return HttpResponse('<marquee><h1>subtraction using - to subtract two numbers</h1></marquee>')