#!/usr/bin/env python3
"""
simple flask app
"""

from flask import Flask, request, jsonify, template_rendered
import os

app = Flask(__name__)

@app.route('/')
def index():
    """simple flask"""
    return template_rendered('0-index.html')