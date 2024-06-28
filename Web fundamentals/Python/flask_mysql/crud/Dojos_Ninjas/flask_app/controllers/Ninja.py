from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo 

from flask_app.models.ninja import Ninja


@app.route('/ninja')
def get_ninjas():
    return render_template('ninja.html',dojo = Dojo.get_all())


@app.route('/create/ninja' , methods=['POST'])
def create():
    Ninja.create(request.form)
    return redirect('/')