#!/usr/bin/python3

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def boardly():
    """Renders the index of the application"""

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)  
