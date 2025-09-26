from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
import logging

from .forms import WorkerForm
from main.models import Worker

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
    return render(request, 'moderator/workers/workers_list.html', {'all_workers': all_workers})
def worker_create(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            logger.warning('Користувач створив робітника')
            return redirect('..')
    form = WorkerForm
    return render(request, 'moderator/workers/create.html', {'form': form})