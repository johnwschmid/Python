from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "secret"

@app.before_first_request
def initial():
	session['gold'] = 0
	session['loot'] = ''

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
	print session['loot']
	if request.form['building'] == 'Farm':
		coins = round(random.randrange(10, 21))
		session['gold'] += coins
		session['loot'] = "Came up on " +str(coins)
	elif request.form['building'] == 'Cave':
		coins = round(random.randrange(5,11))
		session['gold'] += coins
		session['loot'] = "Came up on " +str(coins)
	elif request.form['building'] == 'House':
		coins = round(random.randrange(2,6))
		session['gold'] += coins
		session['loot'] = "Came up on " +str(coins)
	elif request.form['building'] == 'Casino':
		coins = round(random.randrange(-50,51))
		session['gold'] += coins
		session['loot'] = "Came up on " +str(coins)
	return redirect('/')

app.run(debug=True)