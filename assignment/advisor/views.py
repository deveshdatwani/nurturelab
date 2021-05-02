from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create_advisor(*args, **kwargs):
	return HttpResponse("<h1>Hello, World!</h1>")

