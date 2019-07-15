import requests
import json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def listUpcomingMovies():
    movies = getUpcomingMovies()
    json_string = json.dumps([movie.__dict__ for movie in movies])
    return json_string

def getUpcomingMovies():
    movies = []
    allGenres = getGenres()
    apiResponse = requestMoviesAPI()
    for movie in apiResponse:
        image = getMovieImage(movie)
        genres = getMovieGenres(allGenres, movie)
        print(movie)
        movies.append(Movie(movie['title'], image, genres, movie['overview'], movie['release_date']))
    return movies

def getGenres():
    r = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=1f54bd990f1cdfb230adb312546d765d&language=en-US')
    return r.json()['genres']
    
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

def requestMoviesAPI():
    r = requests.get('https://api.themoviedb.org/3/movie/upcoming?api_key=1f54bd990f1cdfb230adb312546d765d&language=en-US&page=1')
    return r.json()['results']

class Movie:
  def __init__(self, title, image, genres, overview, release_date):
    self.title = title
    self.image = image
    self.genres = genres
    self.overview = overview
    self.release_date = release_date
