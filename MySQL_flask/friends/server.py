from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')


@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    print friends
    return render_template('index.html', all_friends = friends)



@app.route('/friends', methods=['POST'])
def create():
    data = {}
    first = request.form['first_name']
    last = request.form['last_name']
    job = request.form['occupation']
    data['first'] = first
    data['last'] = last
    data['job'] = job
    query = 'INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) VALUES(:first, :last, :job, NOW(), NOW())'
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)