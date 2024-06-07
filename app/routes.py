from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

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



from flask import render_template, flash, redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
