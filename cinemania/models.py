from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    # Add more fields for movie details like description, genres, etc.
    # Use Many-to-Many relationships for cast and crew.
    cast = models.ManyToManyField('Person', related_name='movies_as_cast')
    crew = models.ManyToManyField('Person', related_name='movies_as_crew')

class Person(models.Model):
    name = models.CharField(max_length=255)
    # Add more fields for person details like bio, birthdate, etc.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    text = models.TextField()
