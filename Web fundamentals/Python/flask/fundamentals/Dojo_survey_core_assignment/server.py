from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "verystrongkey"  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html')

@app.route('/result')
def result():
    return render_template("result.html",       name=session['name'], dojo_location=session['dojo_location'],  
language= session['language'],comment=session['comment'])
if __name__ == '__main__':
    app.run(debug=True)
    