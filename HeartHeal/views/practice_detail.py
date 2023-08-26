from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View

from HeartHeal.models.user import User
from HeartHeal.models.practice import Practice, Practice_Category, Module, Module_user, get_modules_user, What_yll_learn

class Practice_detail(View):
    def get(self, request, practice_id):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.get_user_by_id(request.session['user'])

        if request.session['role'] == 'doctor':
            return redirect('dashboard')
        
        practice = Practice.objects.get(id=practice_id)
        categories = Practice_Category.objects.all()
        modules = Module.objects.filter(practice=practice)
        what_yll_learns = What_yll_learn.objects.filter(practice=practice)

        data = {
            'current_user' : current_user,
            'categories' : categories,
            'practice' : practice,
            'what_yll_learns' : what_yll_learns,
            'modules' : modules,
        }
        return render(request, 'practice_detail.html', data)
    
    def post(self, request):
        return redirect('practice-detail')
    

class Practice_start(View):
    def get(self, request, practice_id, module_id=0):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.get_user_by_id(request.session['user'])

        if request.session['role'] == 'doctor':
            return redirect('dashboard')
        
        practice = Practice.objects.get(id=practice_id)
        modules = Module.objects.filter(practice=practice)

        if not modules:
            return redirect('practice-home')

        if module_id == 0:
            current_module = modules[0]
        else:
            current_module = modules.get(id=module_id)

        data = {
            'current_user' : current_user,
            'current_practice' : practice,
            'modules' : modules,
            'current_module' : current_module
        }
        return render(request, 'practice_start.html', data)
    
    def post(self, request):
        return redirect('practice-start')
    