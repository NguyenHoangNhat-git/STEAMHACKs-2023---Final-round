from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import BaseDetailView

from django.http import JsonResponse
from django.core import serializers

from django.views import View

from HeartHeal.models.journal import Note
from HeartHeal.models.user import User
from HeartHeal.forms import JournalForm

def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

class Journal(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        journal = Note.objects.filter(user=request.session['user'])
        user = User.objects.filter(id=request.session['user'])[0]
        if not journal:
            new_journal = Note(user=user, content="")
            new_journal.save()
        current_journal = Note.objects.filter(user=request.session['user'])[0]
        return render(request, 'journal.html', {'journal': current_journal})
    
    def post(self, request):
        content = request.POST['content']
        user = User.objects.filter(id=request.session['user'])[0]
        current_journal = Note.objects.filter(user=user)
        current_journal.update(content=content)
        return redirect('journal')
