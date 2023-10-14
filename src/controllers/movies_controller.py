from flask import request, make_response, jsonify

from src.services.movies_service import MoviesService


class MoviesController:


    def __init__(self):
        self.service = MoviesService()


    def get_movies(self):
        movies = self.service.get_movies()
        return make_response(
            jsonify(data=[movie.as_dict() for movie in movies]),
            200
        )
    

    def create_movie(self):
        data = {
            'year': request.json.get('year'),
            'title': request.json.get('title'),
            'studios': request.json.get('studios'),
            'producers': request.json.get('producers'),
            'winner': request.json.get('winner')
        }
                
        self.service.create_movie(data)

        return make_response(
            jsonify(message='Movie created'),
            201
        )
    

    def populate_database(self):
        self.service.populate_database()

        return make_response(
            jsonify(message='Database populated'),
            201
        )