from django.urls import path
from . import views

urlpatterns = [
    path('main_page',views.show_moderator_main_page,name='moderator_main_page'),
    path('login',views.show_login_moderator, name='login_moderator'),
    path('workers/',views.show_workers_list,name='workers_list'),
    path('workers/create',views.worker_create,name='worker_create'),
    path('workers/<int:pk>',views.WorkerDetailView.as_view(),name='worker_details'),
    path('workers/<int:pk>/update',views.WorkerUpdateView.as_view(),name='worker_update'),
    path('workers/<int:pk>/delete',views.WorkerDeleteView.as_view(),name='worker_delete'),
]