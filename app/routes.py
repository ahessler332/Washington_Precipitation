from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')

def index():
    user = {'username': "mug"}
    return render_template('index.html', title='Home', user=user)


