from flask import render_template, redirect , session , request

from flask_app import app

from flask_app.models.user import User 

@app.route('/')
def index():
    if 'userid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
  data = request.form
  if User.validate_registration(data):
      User.create_user(data)
  return redirect('/')

@app.route('/login', methods=["POST"])
def login():
   data = request.form
   if User.validate_login(data):
        user = User.get_by_email(data)
        session['userid'] = user.id
        return redirect('/')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
