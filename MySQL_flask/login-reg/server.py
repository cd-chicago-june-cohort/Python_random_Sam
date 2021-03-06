from flask import Flask, session, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re 
app = Flask(__name__)
mysql = MySQLConnector(app, 'loginreg')
app.secret_key = 'HVZ5T68AE1WF'
import md5

@app.route('/')
def init():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def log():
    valid = True
    #check whether email is in database or not
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    login_data = {'email': email, 'password': password}
    check_query = "SELECT * FROM users WHERE email = :email"
    check = mysql.query_db(check_query, login_data)
    if len(check) == 1:
        #check that password matches that in database
        pw_query = "SELECT password FROM users WHERE email = :email"
        pw = mysql.query_db(pw_query, login_data)
        if password == pw[0]['password']:
            flash('Login Successful!')
            return redirect('/success')
        else:
            flash('Incorrect password. Please try again')
    else:
        flash('Email not in system. Please register before logging in.')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    secure_pw = md5.new(request.form['password']).hexdigest()
    confirmed_pw = request.form['confirm']
    reg_data = {'firstname': firstname, 'lastname': lastname, 'email': email, 'password': secure_pw}
    check_query = "SELECT * FROM users WHERE email = :email"
    check = mysql.query_db(check_query, reg_data)
    if len(check) == 0:
        if password != confirmed_pw:
            flash('Passwords do not match. Please try again')
        elif len(password) < 8:
            flash('Password must be at least 8 characters')
        elif not re.match("^[a-zA-Z0-9_]*$", password):
            flash('Password can only have letters and numbers. Please try again.')
        else:
            query = 'INSERT INTO users(first_name, last_name, email, password) VALUES (:firstname, :lastname, :email, :password)'
            mysql.query_db(query, reg_data)
            flash('Registration successful!')
    else:
        flash('Email is already registered. Use a different email or log in.')
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/logout')
def logout():
    flash('Logout successful')
    return redirect('/')

app.run(debug=True)