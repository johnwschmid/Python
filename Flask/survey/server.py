from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
	print "Got Post Info"
	return render_template('results.html', data_name = request.form['name'],data_loc = request.form['locs'],data_lang = request.form['langs'],data_comment = request.form['comment'])

app.run(debug=True)