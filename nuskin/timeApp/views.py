# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import pdb

# Create your views here.

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('Authenticated successfully!')

				else:
					return HttpResponse('Disabled account')

			else:
				return HttpResponse('Invalid Login')

	else:
		form = LoginForm()

	return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@csrf_exempt
def request_time_off(request):
	# pdb.set_trace()
	if request.method == 'POST':
		req_string = request.read()
		req_type 	= req_string.split('&')[0].split('=')[1]
		username 	= req_string.split('&')[1].split('=')[1]
		timestamp	= req_string.split('&')[2].split('=')[1]

		print'type:', req_type
		print'username:', username
		print'timestamp:', timestamp

		if req_type == 'single':
			print "single"
			print ""
			req_day_off = req_string.split('&')[3].split('=')[1]
			print 'day off:', req_day_off

			# Create RequestedDate entry to database

		if req_type == 'multiple':
			print "multiple"
			print ""
			start_date = req_string.split('&')[3].split('=')[1]
			end_date = req_string.split('&')[4].split('=')[1]
			print "start date:", start_date
			print "end date:", end_date 
			
			# Create RequestedDate entry to database

		else:
			pass


	return HttpResponse('DONE')