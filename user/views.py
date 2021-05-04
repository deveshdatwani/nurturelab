from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from .forms import UserForm
from django.contrib.auth import authenticate

# Create your views here.

@csrf_exempt
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

@csrf_exempt
def login(request, *args, **kwargs):	
	#log a user in 

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		try:
			user_db = User.objects.get(email=email)
		except:
			return JsonResponse({'status':'401','body':'User does not exist.'})
		
		password_db = user_db.password
		
		print(password_db, password)
		if password_db == password:
			id_ = user_db.id
			return JsonResponse({'status':'200_OK','id':id_})
		else:
			return JsonResponse({'status':'401','body':'wrong password'})
	else:
		return render(template_name="user_login", request=request)


