from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from django.views import View
from HeartHeal.models.user import User, Examination, Message

import datetime

def auto_assign(user):
    therapists = User.objects.filter(role='doctor')
    status = Examination.objects.get(patient=user)

    if not user.assigned_doctor:
        max_matches = 0
        current_matches = 0
        for therapist in therapists:
            doc_profile = therapist.doc_profile.splitlines()
            for line in doc_profile:
                if line in status.content:
                    current_matches += 1
                    print(line)
            if current_matches > max_matches or ( current_matches == 0 and max_matches == 0):
                max_matches = current_matches
                user.assigned_doctor = therapist
                user.save()
                print(user.name + " matched with " + therapist.name)
            current_matches = 0

def remove_therapist(request, user_id):
    current_user = User.objects.get(id=user_id)
    messages = Message.objects.filter(
        Q(Q(sender=current_user) & Q(recipient=current_user.assigned_doctor)) |
        Q(Q(sender=current_user.assigned_doctor) & Q(recipient=current_user))
    )
    for message in messages:
        message.delete()
    current_user.assigned_doctor = None
    current_user.save()
    return redirect('dashboard')

class Dashboard(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        current_user = User.get_user_by_id(request.session['user'])

        start_time = datetime.time(13, 0)
        end_time = datetime.time(14, 0)
        current_time = datetime.datetime.now().time()
        all_patients = User.objects.filter(role='patient')
        if start_time <= current_time <= end_time:
            for patient in all_patients:
                auto_assign(patient)

        data = { 'current_user': current_user }
        if (request.session['role'] == 'doctor'):
            data["therapist"] = True
        else:
            data["therapist"] = current_user.assigned_doctor
            
        return render(request, "dashboard.html", data)
    
    def post(self, request):
        # logout
        request.session.clear()
        return redirect('login')