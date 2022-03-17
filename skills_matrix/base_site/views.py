from datetime import datetime
from email import message
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "base_site/home.html")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is an about page")