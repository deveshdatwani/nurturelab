from django.contrib import admin

# Register your models here.
from .models import Advisor, Calls

admin.site.register(Advisor)
admin.site.register(Calls)