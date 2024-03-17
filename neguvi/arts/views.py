from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Стартовая страница")

def art(request):
    return HttpResponse("Тут будут картинки//art")