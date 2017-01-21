from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login')
app.secret_key = "ThisIsSecret!"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create_user():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	valid = True

	if len(first_name) < 3:
		flash("First name must be atleast 3 characters long.")
		valid = False
	if not first_name.isalpha():
		flash("First name can only be alphabetic characters.")
		valid = False
	if len(last_name) < 3:
		flash("Last name must be atleast 3 characters long.")
		valid = False
	if not last_name.isalpha():
		flash("Names can only be alphabetic characters.")
		valid = False
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address.")
		valid = False
	if len(password) < 9:
		flash("Passwords must be atleast 9 characters long.")
		valid = False
	if valid:
		flash("<span>Successully Registered!</span>")
		pw_hash = bcrypt.generate_password_hash(password)
		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
		data = {'first_name': first_name, 'last_name': last_name, 'email': email, 'pw_hash': pw_hash }
		mysql.query_db(query, data)
		return redirect('/')
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']

	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = {'email': email}
	user = mysql.query_db(query, data)
	if user == []:
		flash("Invalid Email Address", "login")
		return redirect('/')
	elif 'user_id' in session:
		if user[0]['id'] != session['user_id']:
			flash("Another User Is Logged In.", "login")
			return redirect('/')
		else:
			if bcrypt.check_password_hash(user[0]['pw_hash'], password):
				session['user_id'] = user[0]['id']
				session['first_name'] = user[0]['first_name']
				session['last_name'] = user[0]['last_name']
				return render_template('login.html')
			else:
				flash("Invalid Password.", "login")
				return redirect('/')
	else:
		if bcrypt.check_password_hash(user[0]['pw_hash'], password):
			session['user_id'] = user[0]['id']
			session['first_name'] = user[0]['first_name']
			session['last_name'] = user[0]['last_name']
			return render_template('login.html')
		else:
			flash("Invalid Password.", "login")
			return redirect('/')

# This app has the added function of denying users from logging in if another user already is logged
# and did not logout.

@app.route('/logout')
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)