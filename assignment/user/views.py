from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.

def register_user(request):
	form = UserForm(request.POST)
	if form.is_valid():
		form.save()
	#u = User.objects.get(id=1)

	return HttpResponse("Hello")
