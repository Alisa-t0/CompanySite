import json
import os
from hashlib import sha256

from django.http import HttpResponse
from dotenv import load_dotenv
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
import logging

from .forms import WorkerForm
from main.models import Worker

load_dotenv()
logger = logging.getLogger('moderator')
class WorkerDetailView(DetailView):
    model = Worker
    template_name = 'moderator/workers/detail_view.html'
    context_object_name = 'worker'

class WorkerUpdateView(UpdateView):
    model = Worker
    template_name = 'moderator/workers/update.html'
    form_class = WorkerForm
    context_object_name = 'worker'

class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'moderator/workers/delete.html'
    context_object_name = 'worker'
    success_url = '..'

def show_moderator_main_page(request):
    logger.info('Користувач перейшов на головну сторінку модератора')
    return render(request, 'moderator/moderator_main_page.html')

def show_workers_list(request):
    logger.info('Користувач перейшов на сторінку списку робітників')
    all_workers = Worker.objects.all()
    sort_field = request.GET.get('sort', 'id')
    direction = request.GET.get('dir', 'asc')

    if request.method == 'GET':
        filter_fields = ['id', 'name', 'surname', 'position', 'salary', 'phone', 'date_hired', 'is_active']
        filters = {}
        for i in filter_fields:
            value = request.GET.get(f'filter_{i}')
            if value:
                filters[i] = value
        all_workers = all_workers.filter(**filters)

    if direction == 'desc':
        all_workers = all_workers.order_by(f'-{sort_field}')
    else:
        all_workers = all_workers.order_by(sort_field)
    return render(request, 'moderator/workers/workers_list.html', {'all_workers': all_workers, 'sort_field': sort_field, 'direction': direction})

def show_login_moderator(request):
    if request.method == 'POST':
        entered_login = sha256(request.POST.get('login').encode()).hexdigest()
        entered_password = sha256(request.POST.get('password').encode()).hexdigest()
        print('hello', entered_login, entered_password)

        correct_login = os.getenv('MYCOMPANY_LOGIN')
        correct_password = os.getenv('MYCOMPANY_PASSWORD')

        if entered_login == correct_login and entered_password == correct_password:
            return redirect('moderator_main_page')
    return render(request, 'moderator/login.html')


def worker_create(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            logger.warning('Користувач створив робітника')
            return redirect('..')
    form = WorkerForm
    return render(request, 'moderator/workers/create.html', {'form': form})

def export_workers(request):
    workers = Worker.objects.all()
    data = {'workers': [{
            'id': worker.id,
            'name': worker.name,
            'surname': worker.surname,
            'position': worker.position,
            'salary': int(worker.salary),
            'phone': worker.phone,
            'date_hired': str(worker.date_hired),
            'is_active': worker.is_active,
            }for worker in workers]}
    with open('workers_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return render(request, 'moderator/export_done.html')

def import_workers(request):
    try:
        with open('workers_data.json', 'r', encoding='utf-8') as file:
            workers = json.load(file)
            for worker_data in workers.get('workers'):
                Worker.objects.get_or_create(id=worker_data['id'],
                        defaults={
                                'name': worker_data['name'],
                                'surname': worker_data['surname'],
                                'position': worker_data['position'],
                                'salary': worker_data['salary'],
                                'phone': worker_data['phone'],
                                'date_hired': worker_data['date_hired'],
                                'is_active': worker_data['is_active'],
                        }
                     )
            return render(request, 'moderator/import_done.html')
    except FileNotFoundError:
        return HttpResponse('<h4>Помилка. Файл не знайдено</h4>')
    except json.JSONDecodeError:
        return HttpResponse('<h4>Помилка. Файл не розпізнано</h4>')
