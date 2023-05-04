from django.shortcuts import render
from django.http import HttpResponse

def Homepage(request):
    return HttpResponse(request,'myapp/homepage.html')