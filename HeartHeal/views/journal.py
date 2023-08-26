from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import BaseDetailView

from django.http import JsonResponse
from django.core import serializers

from django.views import View

from HeartHeal.models.journal import Note
from HeartHeal.models.user import User

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

class Journal(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        current_user = User.get_user_by_id(request.session['user'])
        if current_user.role == 'doctor':
            return redirect('dashboard')

        journal = Note.get_note_by_user(current_user)[0]
        if not journal:
            new_journal = Note(user=current_user, content="")
            new_journal.save()
        current_journal = Note.objects.filter(user=request.session['user'])[0]

        data = {
            'journal': current_journal,
            'current_user': current_user
        }

        return render(request, 'journal.html', data)
    
    def post(self, request):
        content = request.POST['content']
        user = User.objects.filter(id=request.session['user'])[0]
        current_journal = Note.objects.filter(user=user)
        current_journal.update(content=content)
        return redirect('journal')
