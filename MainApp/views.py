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

def home(request):
    author = 'Сиволобов И. В.'
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i> {author} </i>
    """
    return HttpResponse(text)

def about(request):
    person = {'name': 'Иван',
              'fathername': 'Петрович',
              'surname': 'Иванов', 
              'phone_number': '8-923-600-01-02',
              'email': 'vasya@mail.ru'}
    text = f"""
    <ul>
        <li>Имя: <strong>{person['name']}</strong></li>
        <li>Отчество: <strong>{person['fathername']}</strong></li>
        <li>Фамилия: <strong>{person['surname']}</strong></li>
        <li>телефон: <strong>{person['phone_number']}</strong></li>
        <li>email: <strong>{person['email']}</strong></li>
    </ul>
    """
    return HttpResponse(text)

def item(request, id):
    index = None
    for i in items:
        if i['id'] == id:
            index = i
            text = f"""
            <h1>Название: {index['name']}</h1>
            <h1>Количество: {index['quantity']}</h1>
            """ 
            break
        
    if index is None:
        text = f"""
        <h1>Товар с id={id} не найден</h1>
        """
    return HttpResponse(text)