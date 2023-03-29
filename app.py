import os
from flask import Flask, jsonify
from business_logic_layer import list_movies, list_character_names

from flask import jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def list_movies_endpoint():
    sorted_movies = list_movies()
    return jsonify(sorted_movies)

@app.route("/characters/<int:movie_id>", methods=['GET'])
def list_character_names_endpoint(movie_id):
    character_names = list_character_names(movie_id)
    return jsonify(character_names)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
