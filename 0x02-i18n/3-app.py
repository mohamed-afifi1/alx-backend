#!/usr/bin/env python3
"""
simple flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)


class Config:
    """config for app"""
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """set locale based on user's browser preference"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """simple flask"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
