from django.shortcuts import render, HttpResponse
import datetime

def index(request):
	# current_time = datetime.datetime.now()
	context = {
	'time': datetime.datetime.now()
	}
	return render(request, 'timedisplay/index.html', context)