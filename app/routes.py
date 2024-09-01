from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET','POST'])

def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Login request for users {}, remember me={}', format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html ', title='Sign in', form=form)