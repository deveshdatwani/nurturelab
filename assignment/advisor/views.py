from django.shortcuts import render
from django.http import HttpResponse
from .models import Advisor
from .forms import AdvisorForm

# Create your views here.
def create_advisor(request,*args, **kwargs):
	'''form = AdvisorForm(request.POST or None)
	
	if form.is_valid():
		form.save()

	context = {
		"form": form
	}'''
	
	obj = {'object': Advisor.objects.get(id=1)}

	return render(request,"templates/index.html",obj)