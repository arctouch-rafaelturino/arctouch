import requests
import json
import TMDBapi
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/upcomingMovies", methods=['GET'], defaults={'page': 1})
def getUpcomingMovies(page):
    page = request.args.get('page')
    movies = listUpcomingMovies(page)
    jsonString = json.dumps([movie.__dict__ for movie in movies])
    return jsonString

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    movies = listSearchResults(query)
    jsonString = json.dumps([movie.__dict__ for movie in movies])
    return jsonString

@app.route("/movieDetails", methods=['GET'])
def getDetails():
    id = request.args.get('id')
    movie = getMovieDetails(id)
    jsonString = json.dumps(movie.__dict__)
    return jsonString

def listUpcomingMovies(page):
    movies = []
    allGenres = TMDBapi.getAllGenres()
    apiResponse = TMDBapi.getUpcomingMovies(page)
    for movie in apiResponse:
        image = getMovieImage(movie)
        genres = getMovieGenres(allGenres, movie)
        movies.append(Movie(movie['id'], movie['title'], image, genres, movie['release_date']))
    return movies

def listSearchResults(query):
    movies = []
    allGenres = TMDBapi.getAllGenres()
    apiResponse = TMDBapi.getSearchMovies(query)
    for movie in apiResponse:
        image = getMovieImage(movie)
        genres = getMovieGenres(allGenres, movie)
        movies.append(Movie(movie['id'], movie['title'], image, genres, movie['release_date']))
    return movies

def getMovieDetails(id):
    apiResponse = TMDBapi.getMovieDetails(id)
    image = getMovieImage(apiResponse)
    return Movie(apiResponse['id'], apiResponse['title'], image, apiResponse['genres'], apiResponse['release_date'], apiResponse['overview'])

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
  def __init__(self, id, title, image, genres, release_date, overview = None):
    self.id = id
    self.title = title
    self.image = image
    self.genres = genres
    self.release_date = release_date
    self.overview = overview
