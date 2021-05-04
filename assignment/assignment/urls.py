"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from advisor.views import register_advisor, get_advisors, book_call, get_bookings
from user.views import register_user, login

urlpatterns = [
    path('admin/',admin.site.urls),
    path('advisor/register/', register_advisor),
    path('user/register/', register_user),
    path('user/login/', login),
    path('user/advisor/', get_advisors),
    path('user/bookcall/', book_call), #user/<user-id>/advisor<advisor-id>
    path('user/bookings/', get_bookings), #user/<user-id>/<advisor>/<booking>
]
