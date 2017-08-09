from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done

urlpatterns = [
	# url(r'^login/$', views.user_login, name='login'),
	url(r'^$', 						views.dashboard, 		name='dashboard'),
	
	# login /logout urls
	url(r'^login/$', 				login, 					name='login'),
	url(r'^logout/$', 				logout, 				name='logout'),
	url(r'^logout-then-login/$', 	logout_then_login, 		name='logout_then_login'),

	# signup url
	url(r'^signup/$', 				views.signUp, 			name='sign_up'),

	# change password urls
	url(r'^password-change/$', 		password_change, 		name='password_change'),
	url(r'^password-change/done/$', password_change_done, 	name='password_change_done'),

	# request time off endpoint
	# url(r'^time/$',					views.request_time_off,	name='request_time_off'),
	url(r'^dashboard/$',			views.dashboard,		name='request_time_off'),
]