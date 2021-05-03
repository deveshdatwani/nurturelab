from django.shortcuts import render
from django.http import HttpResponse
from .models import Advisor
from .models import Calls
# Create your views here.

def register_advisor(request,*args, **kwargs):
	#insert an advisor in the Advisor table
	if request.method == 'POST':
		return HttpResponse("200_OK")
	else:		
		return render(template_name='register_advisor', request=request)

def get_advisors(request, *args, **kwargs):
	#fetch all advisors from the Advisor table and list them
	obj = {'data':Advisor.objects.all()}
	for i in obj['data']:
		print(i)
		#i['photo_url'] = Advisor.objects.get(name=i.name)
	return render(request=request, template_name="get_advisors", context=obj)

def book_call(request, *args, **kwargs):
	#insert an entry into the Calls table
	
	return HttpResponse("booked your call")

def get_bookings(request, *args, **kwargs):
	#return all user calls
	obj = {'data': Calls.objects.all()}
	return render(template_name="get_bookings", request=request, context=obj)