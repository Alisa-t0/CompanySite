from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_moderator_main_page,name='moderator_main_page'),
    path('workers/',views.show_workers_list,name='workers_list'),
    path('workers/create',views.worker_create,name='worker_create'),
    path('workers/<int:pk>',views.WorkerDetailView.as_view(),name='worker_details'),
    path('workers/<int:pk>/update',views.WorkerUpdateView.as_view(),name='worker_update'),
]