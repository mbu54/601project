# called from __init__.py

from flask import render_template, flash, redirect
# from directory import variable
from app import app
from app.forms import LoginForm

# these @app.route() modify the function below it (they're called decorators)
@app.route('/index', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}'.format(form.author.data))
    return redirect('/index')
  return render_template('login.html', form=form)

