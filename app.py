#!/usr/bin/python3

from os import getenv
from flask import Flask, render_template, make_response, jsonify


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """Handler for a 404 http reponse code"""
    return make_response(jsonify({"message": "not found"}, 404))


@app.route('/', strict_slashes=False, methods=['GET'])
def index():
    """Handler for access to the root"""
    return render_template('index.html')

@app.route('/draw', strict_slashes=False, methods=['GET'])
def draw():
    """Handler for access to the draw appliation"""
    return render_template('draw.html')


if __name__ == "__main__":
    HOST = getenv('BOARDLY_APP_HOST')
    PORT = getenv('BOARDLY_APP_PORT')

    app.run(host=HOST, port=PORT, debug=True)
