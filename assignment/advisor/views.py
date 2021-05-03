from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Advisor
from .models import Calls
from .forms import AdvisorForm
# Create your views here.

def register_advisor(request,*args, **kwargs):

	#insert an advisor in the Advisor table
	if request.method == 'POST':
		form = AdvisorForm(request.POST or None)
		if form.is_valid():
			id_ = form.save()
			obj = {'status':'200_OK', 'advisor-id':id_.id}
			return JsonResponse({'data':obj}, safe=False,)
		else:
			return HttpResponse("400_BAD_REQUEST")
	else:		
		return render(template_name='register_advisor', request=request)

def get_advisors(request, *args, **kwargs):
	
	#fetch all advisors from the Advisor table and list them
	all_advisors = list(Advisor.objects.values()) 
	obj = {'data':{'status':'200_OK', 'body':all_advisors}}
	
	return JsonResponse(obj, safe=False)
	
	#in case it needs to be shown on the wepage
	#return render(request=request, template_name="get_advisors", context=obj)

def book_call(request, *args, **kwargs):
	
	#insert an entry into the Calls table
	if request.method == 'POST':
		form = BookCallForm(request.POST or None)
		if form.is_valid():
			id_ = form.save()
			obj = {'status':'200_OK', 'booking-id':id_}
			return JsonResponse({'data':obj}, safe=False)

	return render(template_name="book_call", request=request)

def get_bookings(request, *args, **kwargs):
	
	#return all user calls
	all_calls = list(Calls.objects.values())
	obj = {'data':{'status':'200_OK', 'body':all_calls}}

	return JsonResponse(obj, safe=False)

	#in case it needs to be shown on the webpage
	#return render(template_name="get_bookings", request=request, context=obj)