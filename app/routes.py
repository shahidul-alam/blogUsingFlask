from app import app
from flask import render_template, flash, redirect , url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET','POST'])

# def index():
#     user = {'username': 'Miguel'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template('index.html', title='Index', user=user, posts=posts)


def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login request for users {}, remember me={}', format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html ', title='Sign in', form=form)