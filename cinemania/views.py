# views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie
import requests
from decouple import config

# Function to fetch additional movie details from the TMDb API
def fetch_movie_details(movie_id):
    api_key = config('TMDB_API_KEY')
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&append_to_response=credits,reviews'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def search(request):
    query = request.GET.get('q', '')

    if query:
        api_key = config('TMDB_API_KEY')
        base_url = 'https://image.tmdb.org/t/p/w500'  # Adjust the size as needed
        url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}&language=en-US'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])

            # Construct the full poster URLs for search results
            for result in results:
                poster_path = result.get('poster_path')
                if poster_path:
                    result['poster_url'] = f'{base_url}{poster_path}'
        else:
            results = []
    else:
        results = []

    return render(request, 'cinemania/search_results.html', {'results': results})

def movie_detail(request, movie_id):
    api_key = config('TMDB_API_KEY')
    base_url = 'https://image.tmdb.org/t/p/w500'  # Adjust the size as needed
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
    response = requests.get(url)

    if response.status_code == 200:
        movie = response.json()
        # Construct the full poster URL
        poster_path = movie.get('poster_path')
        if poster_path:
            movie['poster_url'] = f'{base_url}{poster_path}'
    else:
        movie = None

    return render(request, 'cinemania/movie_detail.html', {'movie': movie})

def movie_list(request):
    api_key = config('TMDB_API_KEY')
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])

        # Construct the full poster URLs
        base_url = 'https://image.tmdb.org/t/p/w500'  # Adjust the size as needed
        for movie in movies:
            poster_path = movie.get('poster_path')
            if poster_path:
                movie['poster_url'] = f'{base_url}{poster_path}'
    else:
        movies = []

    return render(request, 'cinemania/movie_list.html', {'movies': movies})

def home(request):
    api_key = config('TMDB_API_KEY')
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = data.get('results', [])
        
        # Construct the full poster URLs
        base_url = 'https://image.tmdb.org/t/p/w500'  # Adjust the size as needed
        for movie in movies:
            poster_path = movie.get('poster_path')
            if poster_path:
                movie['poster_url'] = f'{base_url}{poster_path}'
    else:
        movies = []

    return render(request, 'cinemania/home.html', {'movies': movies})
