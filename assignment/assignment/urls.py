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
from advisor.views import register_advisor, get_advisors, book_call, get_calls
from user.views import register_user, login

urlpatterns = [
    path('admin/',admin.site.urls),
    path('advisor/register/', register_advisor),
    path('user/register/', register_user),
    path('user/login/', login),
    path('user/<user-id>/advisors/', get_advisors),
    path('user/<user-id>/<advisor-id>/', book_call),
    path('user/<user-id>/advisor/<booking>/', get_calls),
]
