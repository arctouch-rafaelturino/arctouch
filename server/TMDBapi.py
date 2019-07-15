import requests
import key

def getAllGenres():
    r = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key={key.api_key}&language=en-US')
    return r.json()['genres']

def getUpcomingMovies(page):
    r = requests.get(f'https://api.themoviedb.org/3/movie/upcoming?api_key={key.api_key}&language=en-US&page={page}')
    return r.json()['results']

def getSearchMovies(query):
    r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={key.api_key}&language=en-US&page=1&query={query}')
    return r.json()['results']
