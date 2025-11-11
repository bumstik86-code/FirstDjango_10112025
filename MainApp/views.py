from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request) -> HttpResponse:
    context ={
        "name": "Иванов Иван Иванович",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context=context)

def about(request):
    person = {'name': 'Иван',
              'fathername': 'Петрович',
              'surname': 'Иванов',
              'phone_number': '8-923-600-01-02',
              'email': 'vasya@mail.ru'}
    return render(request, "about.html", context=person)

def item(request, id):
    context={'bad_id': id}
    for item in items:
        if item['id'] == id:
            return render(request, "item.html", context=item)
    return render(request, "item.html", context=context)


def items_list(request) -> HttpResponse:
    return render(request, "items.html", context={'goods': items})