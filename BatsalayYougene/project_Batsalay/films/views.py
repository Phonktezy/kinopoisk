from django.shortcuts import render, redirect
from .models import Film, Category

def index(request):
    films = Film.objects.all()
    return render(request, 'index.html', {'films': films})

def add_film(request):
    if request.method == 'POST':

        title = request.POST['title']
        category_id = request.POST['category']
        release_date = request.POST['release_date']
        actors = request.POST['actors']
        show_date = request.POST['show_date']

        film = Film(title=title, category_id=category_id, release_date=release_date, actors=actors, show_date=show_date)
        film.save()

        return redirect('/')
    else:
        category = Category.objects.all()
        return render(request, 'add_film.html', context={"categories": category})

def edit_film(request, film_id):
    film = Film.objects.get(pk=film_id)

    if request.method == 'POST':
        film.title = request.POST['title']
        film.category_id = request.POST['category']
        film.release_date = request.POST['release_date']
        film.actors = request.POST['actors']
        film.show_date = request.POST['show_date']

        film.save()

        return redirect('/')
    else:
        return render(request, 'edit_film.html', {'film': film})

def delete_film(request, film_id):
    film = Film.objects.get(pk=film_id)
    film.delete()
    return redirect('/')