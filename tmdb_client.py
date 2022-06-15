import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmY2UyODVmYWNkOWZlODAzZDQ2MzQwNjM1ZDhkOGNkYyIsInN1YiI6IjYyOGExMThkN2Q1ZGI1MWIyYTllN2IwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DVun-99vTKKrg1HQQVj0k8TCXK97_56wPwCLn0omf1Y"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movie_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmY2UyODVmYWNkOWZlODAzZDQ2MzQwNjM1ZDhkOGNkYyIsInN1YiI6IjYyOGExMThkN2Q1ZGI1MWIyYTllN2IwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DVun-99vTKKrg1HQQVj0k8TCXK97_56wPwCLn0omf1Y"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmY2UyODVmYWNkOWZlODAzZDQ2MzQwNjM1ZDhkOGNkYyIsInN1YiI6IjYyOGExMThkN2Q1ZGI1MWIyYTllN2IwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DVun-99vTKKrg1HQQVj0k8TCXK97_56wPwCLn0omf1Y"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmY2UyODVmYWNkOWZlODAzZDQ2MzQwNjM1ZDhkOGNkYyIsInN1YiI6IjYyOGExMThkN2Q1ZGI1MWIyYTllN2IwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DVun-99vTKKrg1HQQVj0k8TCXK97_56wPwCLn0omf1Y"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

#print(get_popular_movies())

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f' {base_url}{size}{poster_api_path}'

#print(get_poster_url())

def get_movies(how_many, list_type):
    data = get_movie_list(list_type)
    return data["results"][:how_many]

def get_single_movie_cast_20 (how_many, movie_id):
    data = get_single_movie_cast(movie_id)
    return data [:how_many]


