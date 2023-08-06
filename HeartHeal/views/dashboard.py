from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from django.views import View
from HeartHeal.models.user import User

class Dashboard(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        current_user = User.objects.filter(id=request.session['user'])[0]
        return render(request, "dashboard.html", { 'current_user': current_user, "therapist": current_user.assigned_doctor})
    
    def post(self, request):
        # logout
        request.session.clear()
        return redirect('login')