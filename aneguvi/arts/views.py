from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить арт", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

data_db = [
    {'id': 1, 'title': 'Рисунок 1', 'content': '///', 'source': 'arts/images/art1.jpg', 'is_print': False},
    {'id': 2, 'title': 'Рисунок 2', 'content': '//', 'source': 'arts/images/art2.jpg', 'is_print': True},
    {'id': 3, 'title': 'Рисунок 3', 'content': '//', 'source': 'arts/images/art3.jpg', 'is_print': True},
]
# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'arts': data_db,
    }
    return render(request, 'arts/index.html', context=data)

def about(request):
    return render(request, 'base.html', {'title': 'О сайте', 'menu': menu})

def art_for_view(request, arts_id):
    return HttpResponse(f"Отображение арта с id = {arts_id}")

def addpage(request):
    return HttpResponse("addpage")

def contact(request):
    return HttpResponse("contact")

def login(request):
    return HttpResponse("login")

def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")