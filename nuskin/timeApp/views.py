# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import RequestDate
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import pdb

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


def signUp(request):
	return render(request, 'registration/signUp.html', {})


@login_required
def dashboard(request):
	if request.method == 'POST':
		print("YOU POSTED TO '/DASHBOARD'")

		# Get Request String
		req_string = request.read()
		print("request:", req_string.split('&'))

		# Parse Request String
		# csrf_token 	= req_string.split('&')[0].split('=')[1]
		rangeType 	= req_string.split('&')[1].split('=')[1]
		dayType 	= req_string.split('&')[2].split('=')[1]
		username 	= req_string.split('&')[3].split('=')[1]
		startTime	= req_string.split('&')[4].split('=')[1]
		endTime		= req_string.split('&')[5].split('=')[1]
		sickLeave	= False if len(req_string.split('&')) < 7 else True

		print(type(req_string.split('&')))

		print("Range Type:", rangeType)
		print("Day Type:", dayType)
		print("username:", username)
		print("Start Time:", startTime)
		print("End Time:", endTime)
		print("Sick Leave:", str(sickLeave))


		if rangeType == 'single':
			print 'single'
			year = int(startTime.split('-')[0])
			month = int(startTime.split('-')[1])
			day = int(startTime.split('-')[2])
			requestedDate = RequestDate(username=username, 
				start_date = datetime.date(year, month, day), 
				end_date=None, 
				sickLeave= sickLeave,
				halfDay = True if dayType == "half" else False,
				approval_status='PENDING')
			requestedDate.save()

		elif rangeType == 'many':
			print 'many'
			# Create RequestedDate entry to database
			start_year = int(startTime.split('-')[0])
			start_month = int(startTime.split('-')[1])
			start_day = int(startTime.split('-')[2])
			
			end_year = int(endTime.split('-')[0])
			end_month = int(endTime.split('-')[1])
			end_day = int(endTime.split('-')[2])

			requestedDate = RequestDate(username=username, 
				start_date = datetime.date(start_year, start_month, start_day), 
				end_date = datetime.date(end_year, end_month, end_day), 
				sickLeave= sickLeave,
				halfDay = True if dayType == "half" else False,
				approval_status='PENDING')
			requestedDate.save()

	entries = RequestDate.objects.all().filter(username=request.user.username).order_by('-timestamp')

	return render(request, 'account/dashboard.html', {
		'section': 'dashboard',
		'entries': entries
		})
