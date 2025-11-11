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
    text += '\n<a href="/items">назад к списку товаров</a>'
    return HttpResponse(text)

def items_list(request):
    item_list = []
    for index, item in enumerate(items, start=1):
        item_list.append(f'<li><a href="item/{item['id']}">{item['id']}. {item['name']} (Количество: {item['quantity']})</a></li>')

    result = '<ol>'+'\n'.join(item_list) + '\n</ol>'
    return HttpResponse(result)