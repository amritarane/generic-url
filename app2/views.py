from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def morning(request):
    return HttpResponse('<marquee><h1>Hello!!!! GOOD MORNING..... How are you?.....</h1></marquee>')

def night(request):
    return HttpResponse('<marquee><h1>Byee!!!! GOOD NIGHT.....sweet dreams..take care....</h1></marquee>')