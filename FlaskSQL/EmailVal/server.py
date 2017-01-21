from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
	showEmails = mysql.query_db("SELECT * FROM emails")
	return render_template("index.html", allemails = showEmails)

@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("<span>Success!</span>")
		query = "INSERT INTO emails (email, created_at) VALUES (:email,NOW())"
		data = {'email': request.form['email']}
		mysql.query_db(query, data)

	return redirect('/')

app.run(debug=True)