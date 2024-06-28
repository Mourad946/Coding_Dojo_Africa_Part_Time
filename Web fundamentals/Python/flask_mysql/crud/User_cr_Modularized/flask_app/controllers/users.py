from flask_app import app

from flask import render_template , redirect , request

from flask_app.models.user import User

@app.route("/")
def read():
    user = User.get_all()
    return render_template("readall.html",users=user)

@app.route("/users", methods=["POST"])
def create():
    User.create(request.form)
    return redirect ("/")

@app.route("/newuser",methods=["POST"] )
def createNew():
    return render_template ("create.html")

@app.route("/users/<int:id>/delete")
def delete(id):
    data = {"id":id}
    User.delete(data)
    return redirect ("/")
@app.route("/users/<int:id>/update")
def getbyid(id):
    data = {"id":id}
    user = User.get_by_id(data)
    return render_template ("update.html",user=user)

@app.route("/users/update",methods=["POST"])
def update():
    data = {
        "id":request.form["id"],
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]}
    User.update(data)
    return redirect ("/")

@app.route("/users/<int:id>/show")
def show(id):
    data = {"id":id}
    user = User.get_by_id(data)
    return render_template ("readone.html", user=user)