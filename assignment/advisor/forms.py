from django import forms
from .models import Advisor, Calls

class AdvisorForm(forms.ModelForm):
	class Meta:
		model = Advisor
		fields = [
			'name',
			'photo_url'
		]

class BookCallForm():
	class Meta:
		model = Calls
		fields = [
			'advisor',
			'user',
			'datetime'
		]