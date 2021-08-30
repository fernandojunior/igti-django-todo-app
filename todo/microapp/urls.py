from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_todo/', views.edit, name='edit_post'),
    path('edit_todo/<int:id>', views.edit, name='edit'),
    path('clean_todos/', views.clean, name='clean'),
]
