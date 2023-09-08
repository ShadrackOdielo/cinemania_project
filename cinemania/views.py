from django.shortcuts import render, get_object_or_404
from .models import Movie

def search(request):
    query = request.GET.get('q')
    results = Movie.objects.filter(title__icontains=query)
    # You can expand this to search in other fields and across multiple models
    return render(request, 'cinemania/search_results.html', {'results': results})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # You can fetch additional related data here (cast, crew, reviews, etc.)
    return render(request, 'cinemania/movie_detail.html', {'movie': movie})
