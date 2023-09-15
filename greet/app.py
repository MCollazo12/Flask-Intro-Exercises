"""
Handles the responses to the routes below
"""
from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def display_welcome():
    return 'Welcome'

@app.route('/welcome/home')
def display_home():
    return 'Welcome home'

@app.route('/welcome/back')
def display_welcome_back():
    return 'Welcome back'
