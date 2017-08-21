from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "neww"

@app.route('/')
def start():
    if 'target' not in session:
        session['target'] = random.randrange(0,101)
        print session['target']
    print session
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    session['guess'] = int(request.form['please'])
    if request.method == 'POST':
        x = session['guess']
        if x > session['target']:
            session['instruction'] = 'high'
            print '1'
        elif x < session['target']:
            session['instruction'] = 'low'
            print '2'
        else:
            session['instruction'] = 'correct'
    return redirect('/')

@app.route('/restart')
def restart():
    session.pop('target')
    session.pop('guess')
    session.pop('instruction')
    return redirect('/')

app.run(debug=True)