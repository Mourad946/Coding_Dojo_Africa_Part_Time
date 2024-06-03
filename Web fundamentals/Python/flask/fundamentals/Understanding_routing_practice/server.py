from flask import Flask, abort

app = Flask(__name__)

# Route for "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World!"

# Route for "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Dynamic route for greeting with names
@app.route('/say/<name>')
def say(name):
    if not name.isalpha():
        abort(404)
    return f"Hi {name.capitalize()}!"

# Dynamic route for repeating words
@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    if not word.isalpha():
        abort(404)
    return (word + ' ') * num

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)