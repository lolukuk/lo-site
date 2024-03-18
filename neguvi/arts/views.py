from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Стартовая страница")
def art(request, art_id):
    return HttpResponse(f"Тут будут картинки//art<p>id: {art_id}</p>")

def art_by_slug(request, art_slug):
    return HttpResponse(f"Тут будут картинки//art<p>slug: {art_slug}</p>")

def archive(request, year):
    return HttpResponse(f"Тут будут картинки//art<p>{year}</p>")