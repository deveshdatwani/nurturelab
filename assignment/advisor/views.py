from django.shortcuts import render
from django.http import HttpResponse
from .models import Advisor
from .forms import AdvisorForm

# Create your views here.
def register_advisor(request,*args, **kwargs):
	#inser an advisor in the Advisor table
	
	form = AdvisorForm(request.POST or None)
	
	if form.is_valid():
		form.save()
		return HttpResponse("200_OK")

	else:
		return HttpResponse("400_BAD_REQUEST")

def get_advisors(request, *args, **kwargs):
	#fetch all advisors from the Advisor table and list them
	
	obj = Advisor.objects.get()

	return HttpResponse("all advisors")

def book_call(request, *args, **kwargs):
	#insert an entry into the Calls table
	return HttpResponse("booked your call")