from django.urls import path
from . import views
urlpatterns = [
    path('', views.main_page, name='home'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contacts/', views.contacts, name='contacts'),
]