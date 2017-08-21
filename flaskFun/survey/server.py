from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def info():
    name = request.form['name']
    city = request.form['loc']
    lang = request.form['lang']
    comments = request.form['comments']
    return render_template('info.html', n = name, c = city, l = lang, com = comments)

@app.route('/back')
def go_back():
    return render_template('index.html')


app.run(debug=True)