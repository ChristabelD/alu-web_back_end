#!/usr/bin/env python3

"""
This is a basic Flask application with
internationalization support using Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


# Instantiate Babel object
babel = Babel(app)


class Config:
    """
    Configuration class for the Flask app.
    """
    # Define available languages
    LANGUAGES = ['en', 'fr']
    # Set default locale and timezone
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config as config for the Flask app
app.config.from_object(Config)

# Define get_locale function using babel.localeselector decorator
@babel.localeselector
def get_locale():
    """
    Determine the best match with supported languages
    based on request.accept_languages,
    """
    # Check if the 'locale' parameter is present in the URL
    # and if its value is a supported locale
    if 'locale' in request.args and \
            request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    else:
        # Resort to the default behavior
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index template.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
   