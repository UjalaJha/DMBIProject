from django.shortcuts import render
from django.conf import settings
# from polyline import views
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth import views as auth_views
from django.views.generic import View
#from .forms import UserForm
from django.http import HttpResponse
import csv
import json




# Create your views here.
def index(request):
	print("hiii")
	return render(request,'polyline/index.html')


def dashboard(request):
	return render(request,'polyline/dashboard.html')

def analytics(request):
	return render(request,'polyline/analytics.html')

def polyline(request):
	data=[]
	data.append('2018-10-29T19:24:04+00:00')
	data.append('10')
	data.append('1')
	# print(data)
	context = {
		'range': range(20),
		'data': data
	}
	return render(request,'polyline/polyline.html',context)


def map(request):
	data = PolylineData.objects.all()
	locations = []
	for f in data:
		locationcol = {}
		if f.score >=0 and f.score <=33.33:
			color = 'green'
		elif f.score >33.33 and f.score <=66.66:
			color = 'yellow'
		else:
			color = 'red'
		
		with open('{}\\'.format(settings.MEDIA_ROOT) + f.filename) as k:
			lis = []
			x = list(csv.reader(k))
			for y in x:
				d = {}
				d['lat'] = float(y[0])
				d['lng'] = float(y[1])
				lis.append(d)
			
		locationcol['location'] = lis
		locationcol['color'] = color
		locations.append(locationcol)
			
	context = {
		'locations': locations
	}
	return render(request,'polyline/map.html', context)

def sessionfn(request):
	return HttpResponse(request.session)
	# print(request.session)
	
def convert(request):
	data = PolylineData.objects.all()
	locations = []
	for f in data:
		locationcol = {}
		if f.score >=0 and f.score <=33.33:
			color = 'green'
		elif f.score >33.33 and f.score <=66.66:
			color = 'yellow'
		else:
			color = 'red'
		
		with open('{}\\'.format(settings.MEDIA_ROOT) + f.filename) as k:
			lis = []
			x = list(csv.reader(k))
			for y in x:
				d = {}
				d['lat'] = float(y[0])
				d['lng'] = float(y[1])
				lis.append(d)
			
		locationcol['location'] = lis
		locationcol['color'] = color
		locations.append(locationcol)
			
	context = {
		'locations': locations
	}
	return render(request,'polyline/showmap.html', context)
	# return HttpResponse(json.dumps(locations))
