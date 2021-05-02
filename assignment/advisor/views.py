from django.shortcuts import render
from django.http import HttpResponse
from .models import Advisor

# Create your views here.
def create_advisor(request,*args, **kwargs):
	obj = Advisor.objects.get(name="devesh datwani")
	context = {
		"obj":obj
	}
	return render(context)