from django.shortcuts import render

# Create your views here.
def main_page(request):
    return render(request, 'main/main_page.html')

def services(request):
    return render(request, 'main/services.html')

def projects(request):
    return render(request, 'main/projects.html')

def contacts(request):
    return render(request, 'main/contacts.html')
