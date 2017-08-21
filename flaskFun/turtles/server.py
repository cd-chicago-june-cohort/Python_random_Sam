from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def turtle_pick(color):
    return render_template("turtles.html", pic = color)

app.run(debug=True)