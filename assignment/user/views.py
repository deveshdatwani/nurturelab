from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from .forms import UserForm

# Create your views here.

def register_user(request, *args, **kwargs):
	#create a user

	if request.method == 'POST':
		form = UserForm(request.POST or None)
		
		if form.is_valid():
			form.save()
			name, email = form.cleaned_data['name'], form.cleaned_data['email']
			obj = {'status':'200_OK'}
			obj['user-id'] = User.objects.get(name=name,email=email).id
			
			return JsonResponse({'data':obj})
		
		else: 
			return JsonResponse({"data":"400_BAD_REQUEST"})
	
	else: 
		return render(template_name='register_user', request=request)

def login(request, *args, **kwargs):	
	#log a user in 

	if request.method == 'POST':
		auth = request.POST()
		
		if auth.is_valid():
			None
		else:
			return JsonResponse({"data":"400_BAD_REQUEST"})
	
	else:
		return render(template_name="user_login", request=request)


