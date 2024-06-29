from flask import render_template , redirect, session , request

from flask_app import app

from flask_app.models.user import User

from flask_app.models.recipe import Recipe
from flask_app.controllers import Users

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_id = {"id":session["user_id"]}
    user = User.get_by_id(user_id)
    receipes = Recipe.get_all()
    return render_template('dashboard.html', user=user, receipes=receipes)
@app.route('/receipe/new')
def new():
    if 'user_id' not in session:
        return redirect('/')
    user_id = {"id":session["user_id"]}
    user = User.get_by_id(user_id)
    return render_template('new_recipe.html', user=user)

@app.route('/receipe/create', methods=['POST'])
def create():
    if 'user_id' not in session:
        return redirect('/')
    Recipe.create(request.form)
    return redirect('/dashboard')
