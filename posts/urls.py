from django.urls import path
from .views import post_list
from . import views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/edit/', views.post_edit, name = 'post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name = 'post_delete'),
    path('post/<int:pk>/detail/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]