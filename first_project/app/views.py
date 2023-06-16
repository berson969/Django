from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        # 'Показать текущее время': reverse('time'),
        # 'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    time_now = datetime.datetime.now()
    current_time = time_now.strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir(request):
    pass

