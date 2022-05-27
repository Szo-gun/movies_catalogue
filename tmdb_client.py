import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmY2UyODVmYWNkOWZlODAzZDQ2MzQwNjM1ZDhkOGNkYyIsInN1YiI6IjYyOGExMThkN2Q1ZGI1MWIyYTllN2IwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.DVun-99vTKKrg1HQQVj0k8TCXK97_56wPwCLn0omf1Y"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
    
#print(get_popular_movies())

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f' {base_url}{size}{poster_api_path}'

#print(get_poster_url())

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


