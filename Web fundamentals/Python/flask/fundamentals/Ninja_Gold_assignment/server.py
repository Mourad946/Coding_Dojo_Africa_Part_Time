from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'keep_it_secret_keep_it_safe'

BUILDINGS = {
    'farm': (10, 20),
    'cave': (5, 10),
    'house': (2, 5),
    'casino': (-50, 50)
}

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    if 'moves' not in session:
        session['moves'] = 0

    win_message = ""
    if session['gold'] >= 500:
        if session['moves'] <= 15:
            win_message = "Congratulations! You've won the game in {} moves!".format(session['moves'])
        else:
            win_message = "You have reached 500 gold, but it took more than 15 moves."

    return render_template('index.html', gold=session['gold'], activities=session['activities'], win_message=win_message)

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    gold_range = BUILDINGS[building]
    gold_earned = random.randint(gold_range[0], gold_range[1])
    
    session['gold'] += gold_earned
    session['moves'] += 1

    activity = f"Earned {gold_earned} gold from the {building}! ({datetime.now().strftime('%Y/%m/%d %I:%M %p')})"
    if gold_earned < 0:
        activity = f"Entered a casino and lost {abs(gold_earned)} gold... Ouch... ({datetime.now().strftime('%Y/%m/%d %I:%M %p')})"
    session['activities'].insert(0, activity)  # Insert at the beginning for descending order

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


