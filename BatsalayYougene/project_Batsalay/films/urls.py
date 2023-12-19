from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_film, name='add_film'),
    path('edit/<int:film_id>/', views.edit_film, name='edit_film'),
    path('delete/<int:film_id>/', views.delete_film, name='delete_film'),
]
