from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.dojo import Dojo

from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    data = Dojo.get_all()
    return render_template('dojo.html',dojo=data)

@app.route('/show/<int:id>')
def show(id):
    data = {'id':id}
    return render_template('show.html',dojo= Dojo.get_ninjafrom(data))

@app.route('/adddojo' , methods=['POST'])
def adddojo():
    Dojo.create(request.form)
    return redirect('/')