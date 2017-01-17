from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "name"

@app.before_first_request
def before():
	session['count'] = 0

@app.route('/')
def func():
	return render_template('index.html')

@app.route('/ninjas')
def ninjas():
	session['count'] += 2
	return redirect('/')

@app.route('/hackers')
def hackers():
	session['count'] = 1
	return redirect('/')

app.run(debug=True)