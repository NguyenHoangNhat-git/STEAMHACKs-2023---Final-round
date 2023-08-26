from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View

from HeartHeal.models.user import User
from HeartHeal.models.practice import Practice, Practice_Category, Module, Module_user, get_modules_user

class Practice_home(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.get_user_by_id(request.session['user'])

        if request.session['role'] == 'doctor':
            return redirect('dashboard')
        
        categories = Practice_Category.objects.all()
        all_practices = Practice.objects.all()

        data = {
            'current_user' : current_user,
            'categories' : categories,
            'practices' : all_practices
        }
        return render(request, 'practice_home.html', data)
    
    def post(self, request):
        return redirect('practice-home')
    

class Practice_done(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.get_user_by_id(request.session['user'])

        if request.session['role'] == 'doctor':
            return redirect('dashboard')
        data = {

        }
        return render(request, 'practice_done.html', data)
    
    def post(self, request):
        return redirect('practice-done')
    

class Practice_current(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.get_user_by_id(request.session['user'])

        if request.session['role'] == 'doctor':
            return redirect('dashboard')
        data = {

        }
        return render(request, 'practice_current.html', data)
    
    def post(self, request):
        return redirect('practice-current')