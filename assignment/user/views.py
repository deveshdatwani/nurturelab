from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register_user(request, *args, **kwargs):
	
	#create a user
	if request.method == 'POST':
		None
	else:
		return render(template_name='register_user', request=request)

def login(request, *args, **kwargs):
	
	#login a user
	if request.method == 'POST':
		#check credentials of the form filled
		auth = request.POST()
		
		if auth.is_valid():
			None
			#return HttpResponse("200_OK")
		else:
			return HttpResponse("400_BAD_REQUEST")
	
	#return the form for loggin in when GET request is made from the browser
	else:
		return render(template_name="user_login", request=request)


