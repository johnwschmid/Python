from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.before_first_request
def before():
	session['rando'] = random.randrange(0,101)
	session['bgc'] = 'orange'
	session['message'] = "DO YOUR WORST SILLYMAN!"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/game', methods = ['POST'])
def guess():

	if int(request.form['guess']) == session['rando']:
		session['message'] = 'You guessed correct!'
		session['bgc'] = 'green'

	elif int(request.form['guess']) < session['rando']:
		session['message'] = 'Your guess was too low.'
		session['bgc'] = 'blue'

	elif int(request.form['guess']) > session['rando']:
		session['message'] = 'Your guess was too high.'
		session['bgc'] = 'red'

	return redirect('/')

app.run(debug=True)