from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View

from HeartHeal.models.user import User, Message, if_user_send

class chat_rooms(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        current_user = User.get_user_by_id(request.session['user'])

        if current_user.role == 'patient':
            return redirect('chat-room', str(current_user.id) + "_" + str(current_user.assigned_doctor.id))
        
        elif current_user.role == 'doctor':
            patients = User.get_all_patient(current_user)
            data = {
                'patients' : patients
            }
            return render(request, 'chat_rooms.html', data)
        
    def post(self, request):
        request.session['patient'] = request.POST['patient']

        current_user = User.get_user_by_id(request.session['user'])
        patient = User.get_user_by_id(request.session['patient'])
        return redirect('chat-room', str(patient.id) + "_" + str(current_user.id))


# not the POST (message)
def chat_room_user(request, room_name):
    if ('user' not in request.session):
        return redirect('login')
    
    current_user = User.get_user_by_id(request.session['user'])
    if current_user.role == 'patient':
        # get all messages that current user is in with the therapist
        messages_related = Message.objects.filter(
            (Q(sender=current_user) & Q(recipient=current_user.assigned_doctor)) |
            (Q(sender=current_user.assigned_doctor) & Q(recipient=current_user))
            ).order_by('timestamp')
        other_person = current_user.assigned_doctor
    
    else: 
        if 'patient' not in request.session:
            return redirect('chat-room')
        patient = User.get_user_by_id(request.session['patient'])
        messages_related = Message.objects.filter(
            (Q(sender=current_user) & Q(recipient=patient)) |
            (Q(sender=patient) & Q(recipient=current_user))
            ).order_by('timestamp')
        other_person = patient

    messages = [{"message" : message, "if_user_send": if_user_send(current_user, message) } for message in messages_related]

    data = {
        'messages': messages, 
        'current_user' : current_user,
        'other_person' : other_person,
        "room_name": room_name,
        'current_user_id': current_user.id
        }
    if current_user.role == 'doctor':
        patients = User.get_all_patient(current_user)
        data['patients'] = patients


    return render(request, "chat_room.html", data)
