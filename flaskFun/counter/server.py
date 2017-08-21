from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "start over"

@app.route('/')
def load():
    if 'count_num' not in session:
        session['count_num'] = 0
    return render_template('index.html', count = session['count_num'])

@app.route('/reload')
def view_count():
    count = session['count_num']
    count += 1
    session['count_num'] = count
    return render_template('index.html', count = session['count_num'])

@app.route('/two')
def view_count_plus_two():
    count = session['count_num']
    count += 2
    session['count_num'] = count
    return render_template('index.html', count = session['count_num'])

@app.route('/clear')
def clear():
    count = session['count_num']
    count = 0
    session['count_num'] = count
    return render_template('index.html', count = session['count_num'])

app.run(debug=True)