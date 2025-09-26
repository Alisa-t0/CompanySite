from django.shortcuts import render, redirect

from .forms import WorkerForm
from main.models import Worker


# Create your views here.
def show_moderator_main_page(request):
    return render(request, 'moderator/moderator_main_page.html')

def show_workers_list(request):
    all_workers = Worker.objects.all()
    return render(request, 'moderator/workers/workers_list.html', {'all_workers': all_workers})
def worker_create(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('..')
    form = WorkerForm
    return render(request, 'moderator/workers/create.html', {'form': form})