import requests
import json
import TMDBapi
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'], defaults={'page': 1})
def getUpcomingMovies(page):
    page = request.args.get('page')
    movies = listUpcomingMovies(page)
    json_string = json.dumps([movie.__dict__ for movie in movies])
    return json_string

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    movies = listSearchResults(query)
    json_string = json.dumps([movie.__dict__ for movie in movies])
    return json_string


def listUpcomingMovies(page):
    movies = []
    allGenres = TMDBapi.getAllGenres()
    apiResponse = TMDBapi.getUpcomingMovies(page)
    for movie in apiResponse:
        image = getMovieImage(movie)
        genres = getMovieGenres(allGenres, movie)
        movies.append(Movie(movie['title'], image, genres, movie['overview'], movie['release_date']))
    return movies

def listSearchResults(query):
    movies = []
    allGenres = TMDBapi.getAllGenres()
    apiResponse = TMDBapi.getSearchMovies(query)
    for movie in apiResponse:
        image = getMovieImage(movie)
        genres = getMovieGenres(allGenres, movie)
        movies.append(Movie(movie['title'], image, genres, movie['overview'], movie['release_date']))
    return movies

def getMovieGenres(genres, movie):
    movieGenres = []
    for genre_id in movie['genre_ids']:
        movieGenres.append(getGenreNameById(genres, genre_id))
    return movieGenres

def getGenreNameById(genres, id):
    for genre in genres:
        if(genre['id'] == id):
            return genre['name']
    return 'Genre not found'

def getMovieImage(movie):
    if('poster' in movie):
        return movie['poster_path']
    return movie['backdrop_path']


class Movie:
  def __init__(self, title, image, genres, overview, release_date):
    self.title = title
    self.image = image
    self.genres = genres
    self.overview = overview
    self.release_date = release_date
