from django.shortcuts import render, redirect
from django.http import HttpResponse

from HeartHeal.models.user import User

def home(request):
    if 'user' in request.session:
        return redirect('home-me')
    return render(request, 'home.html')

def home_me(request):
    return render(request, 'home_me.html')