from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_user(request):
	form = UserCreationForm()
	obj = {"form":form}
	return render(request, "templates/index.html", obj)


