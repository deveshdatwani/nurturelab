from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def register_user(request):

	#u = User.objects.get(id=1)

	return HttpResponse("Hello")
