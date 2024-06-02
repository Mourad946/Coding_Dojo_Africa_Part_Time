from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/play")
def play():
    # Default to 3 boxes
    num_boxes = 3 
    color = 'blue'  # Default color

    return render_template("index.html", num_boxes=num_boxes, box_color=color)

@app.route("/play/<int:x>")
def play_x(x):
    color = 'blue'  # Default color
    return render_template("index.html", num_boxes=x, box_color=color)  

@app.route("/play/<int:x>/<color>")
def play_x_color(x, color):
    return render_template("index.html", num_boxes=x, box_color=color) 

if __name__ == '__main__':
    app.run(debug=True)