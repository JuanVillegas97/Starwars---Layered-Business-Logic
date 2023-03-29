import requests

movie_url = "https://swapi.dev/api/films/"

def list_movies():
    data = requests.get(movie_url).json()
    movies= []
    for movie in data["results"]:
        movies.append({
            "id": movie["episode_id"], 
            "name": movie["title"]
        })
    sorted_movies = sorted(movies, key=lambda x: x['id'])
    return sorted_movies

def list_character_names(movie_id):
    data = requests.get(movie_url).json()
    character_urls = []
    for movie in data["results"]:
        if movie["episode_id"] == movie_id:
            character_urls = movie["characters"]

    character_names = []
    for url in character_urls:
        person = requests.get(url).json()
        name = person["name"]
        character_names.append(name)

    return character_names
