from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.http import JsonResponse
from django.core import serializers

from django.views import View
from django.db.models import Q
from django.db.models.functions import Concat
from django.db.models import Value

from HeartHeal.models.user import User, Message

import datetime

def if_patient_send(patient, message):
    return message.sender == patient

class Chat(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.objects.filter(id=request.session['user'])[0]

        # get all conversations that current user is in
        messages_related = Message.objects.filter(
            (Q(sender=current_user) & Q(recipient=current_user.assigned_doctor)) |
            (Q(sender=current_user.assigned_doctor) & Q(recipient=current_user))
            ).order_by('timestamp')
        conversation = [{"message" : message, "if_patient_send": if_patient_send(current_user, message) } for message in messages_related]

        return render(request, "chat.html", {'conversation': conversation, 'therapist' : current_user.assigned_doctor})
    
    def post(self, request):
        content = request.POST['content']
        current_user = User.objects.filter(id=request.session['user'])[0]
        if content:
            new_message = Message(sender=current_user, recipient=current_user.assigned_doctor, content=content, timestamp=datetime.datetime.now())
            new_message.save()
        return redirect("chat")
    
