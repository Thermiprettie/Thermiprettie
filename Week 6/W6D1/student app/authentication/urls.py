
from django.contrib import admin
from django.urls import path, include
from .views import Register

urlpatterns = [
 path('', include('django.contrib.auth.urls')),
 path('register', Register, name = 'register'), #call out register function in views.py. #name=register means our register button will redirect us to the registration link
    
    
]
