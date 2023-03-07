from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstproject(request):
    return HttpResponse('<h2> my first function</h2>')



def secondproject(request):
    return HttpResponse('<h2> my second function</h2>')