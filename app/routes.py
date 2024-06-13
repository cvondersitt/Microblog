from app import app, db
from app.forms import LoginForm
from app.models import User
from flask import request, render_template, flash, redirect, url_for
from urllib.parse import urlsplit
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa


@app.route('/')
@app.route('/index')
@login_required
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
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))