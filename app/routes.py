from app import app
from flask import render_template, flash, redirect , url_for , request
from app.forms import LoginForm
from flask_login import current_user, login_user , login_required
from app.models import User
from urllib.parse import urlsplit

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET','POST'])
@app.route('/logout')

@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Index', user=user, posts=posts)


def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form= LoginForm()
    if form.validate_on_submit():
        user= db.session.scalar(
            sa.select(user).where(User.username==form.username.data))
        if user is None or not user.check.password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(user , remember= form.remember_me.data)
        next_page= request.args.get('next')
        if not next_page or urlsplit(next_page).netloc !='':
            next_page= url_for('index')
        return redirect(next_page)
    return render_template('login.html ', title='Sign in', form=form)

def logout():
    logout_user()
    return redirect(url_for('index'))
