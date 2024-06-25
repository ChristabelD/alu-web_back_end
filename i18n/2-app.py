#!/usr/bin/env python3

"""
This is a basic Flask application with internationalization
support using Flask-Babel.
"""

from flask import Config, Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


# Store babel object in a variable named babel.
babel = Babel(app)


class Config:
    """" create a Config class with
     the specified attributes.
    """
    # Define available languages
    LANGUAGES = ['en', 'fr']
    # Set default locale and timezone
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


# Define get_locale function using babel.localeselector decorator
@babel.localeselector
def get_locale():
    """
    Determine the best match with supported languages
    based on request.accept_languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index() -> str:
    """The home/index page.
    """
    return render_template('2-index.html')


"""run the flask app"""


if __name__ == '__main__':
    app.run(debug=True)
