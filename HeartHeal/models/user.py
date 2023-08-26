from django.db import models
from django.db.models import Q

ROLE = [
    ('patient', 'patient'),
    ('doctor', 'doctor')
]

class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, default=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    image = models.ImageField(upload_to='imgs/', blank=True, null=True)
    assigned_doctor = models.ForeignKey('self',on_delete=models.CASCADE, blank=True, null=True)

    role = models.CharField(max_length=10, choices=ROLE, default='patient')
    doc_profile = models.TextField(null=True, blank=True)

    def register(self):
        self.save()

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
        
    def get_user_by_id(id):
        try:
            return User.objects.get(id=id)
        except:
            return False

    def get_all_patient(therapist):
        try:
            return User.objects.filter(assigned_doctor=therapist)
        except:
            return False

    def is_Exists(self):
        if User.objects.filter(email=self.email):
            return True

        return False


class Examination(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.patient.name + "'s mental status"
    

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    def get_latest_message(self, sender_id, recipient_id):
        return Message.filter(Q(sender=sender_id) & Q(recipient=recipient_id))[0]


def if_user_send(current_user, message):
    return message.sender == current_user