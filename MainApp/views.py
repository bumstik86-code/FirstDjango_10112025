from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
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