from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cole'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author':{'username': 'Jack'},
            'body': 'I like books!'
        },
        {
            'author':{'username': 'Ivan'},
            'body': 'Smoothies taste good on Tuesdays!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
