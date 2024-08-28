from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = [
    {'title': 'About the site', 'url_name': 'about'},
    {'title': 'Add an article', 'url_name': 'add_page'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'LogIn', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Bitcoin', 'content': 'Info about the Bitcoin', 'is_published': True},
    {'id': 2, 'title': 'Ethereum', 'content': 'Info about the Ethereum', 'is_published': True},
    {'id': 3, 'title': 'TON', 'content': 'Info about the TON', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Main page',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'crypto/index.html', context=data)


def show_post(request, post_id):
    return HttpResponse(f'Show the post with ID = {post_id}')


def about(request):
    data = {
        'title': 'About the site',
        'menu': menu,
    }
    return render(request, 'crypto/about.html', context=data)


def addpage(request):
    return HttpResponse('Add the post')


def contact(request):
    return HttpResponse('Contact')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
