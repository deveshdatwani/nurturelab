from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Advisor, Calls
from .forms import AdvisorForm, BookCallForm
from django.urls import reverse
from user.models import User
# Create your views here.


@csrf_exempt
def register_advisor(request,*args, **kwargs):
	#insert an advisor in the Advisor table
	
	if request.method == 'POST':
		form = AdvisorForm(request.POST or None)
		print(request.POST)
		
		if form.is_valid():
			id_ = form.save()
			obj = {'status':'200_OK', 'advisor-id':id_.id}

			return JsonResponse({'data':obj}, safe=False,)
		
		else:
			return HttpResponse("400_BAD_REQUEST")
	
	else:		
		return render(template_name='register_advisor', request=request)


@csrf_exempt
def get_advisors(request, *args, **kwargs):	
	#fetch all advisors from the Advisor table and list them

	query_set = list(Advisor.objects.values()) 
	obj = {'data':{'status':'200_OK', 'body':query_set}}
	
	return JsonResponse(obj, safe=False)
	#in case it needs to be shown on the wepage
	#return render(request=request, template_name="get_advisors", context=obj)


@csrf_exempt
def book_call(request, *args, **kwargs):	
	#insert an entry into the Calls table

	if request.method == 'POST':
		print(request.POST)
		url = request.get_full_path().split('/')
		userid = url[2]
		advisorid = url[4]
		
		try:
			user = User.objects.get(id=userid)
		except User.objects.DoesNotExist:
			raise Http404

		try:
			advisor = Advisor.objects.get(id=advisorid)
		except Advisor.objects.DoesNotExist:
			raise Http404

		print(dir(request.POST))
		#datetime = request.POST
		#Calls.objects.create(user=user.name, advisor=advisor.name, datetime=datetime)
		
	return render(template_name="book_call", request=request)


@csrf_exempt
def get_bookings(request, *args, **kwargs):	
	#return all user calls

	query_set = list(Calls.objects.values())
	response = {'data':query_set}

	return JsonResponse(response)

	#in case it needs to be shown on the webpage
	#return render(template_name="get_bookings", request=request, context=response)






