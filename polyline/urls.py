from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name='polyline'
from .views import *

urlpatterns=[

	url(r'^$',views.map,name="index"),
]
'''
{'template_name': 'pothole/success.html'}
'''