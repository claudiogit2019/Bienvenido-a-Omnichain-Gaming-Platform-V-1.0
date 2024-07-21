# my_project/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the home page")

def assets(request):
    return HttpResponse("This is the assets page")

def coins(request):
    return HttpResponse("This is the coins page")
