from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def index(request): #HttpRequest
    return HttpResponse("Стартовая страница")
def art(request, art_id):
    return HttpResponse(f"Тут будут картинки//art<p>id: {art_id}</p>")

def art_by_slug(request, art_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"Тут будут картинки//артыы<p>slug: {art_slug}</p>")

def archive(request, year):
    if year > 2024:
        raise Http404()
    return HttpResponse(f"Тут будут картинки//archive<p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")