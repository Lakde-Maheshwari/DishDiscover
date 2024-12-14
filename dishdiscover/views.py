from django.http import HttpResponse
from . import views
from django.shortcuts import render

def home(request):
    return render(request,"base.html")