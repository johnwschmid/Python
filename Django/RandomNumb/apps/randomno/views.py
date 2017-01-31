from django.shortcuts import render, redirect
import random

def index(request):
	if not 'attempt' in request.session:
		request.session['attempt'] = 0
		request.session['word'] = 'Click Generate to Begin.'
	return render(request, 'randomno/index.html')

def generate(request):
	randomword = ''
	vowels = ['a','e','i','o','u']
	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','t','v','w','x','y','z']

	for i in range(7):
		cons_index = random.randint(0,len(consonants)-1)
		randomword += consonants[cons_index]
		vow_index = random.randint(0,len(vowels)-1)
		randomword += vowels[vow_index]

	request.session['attempt'] += 1
	request.session['word'] = randomword

	return redirect('/')