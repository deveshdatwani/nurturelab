from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from .forms import UserForm

# Create your views here.

def register_user(request, *args, **kwargs):
	form = UserForm(request.POST or None)
	#create a user
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			name, email = form.cleaned_data['name'], form.cleaned_data['email']
			obj = {'status':'200_OK'}
			obj['user-id'] = User.objects.get(name=name,email=email).id
			return JsonResponse({'data':obj})
		else:
			return HttpResponse("400_BAD_REQUEST")
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


