from django.db import models
import datetime, calendar
from django.db.models import Q

from .user import User

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    when = models.IntegerField()
    duration = models.DurationField(default=datetime.time(hour=1))
    link_meeting = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     self.duration = self.duration.total_seconds() / 60
    #     self.meeting_time = self.meeting_time.replace(second=0, microsecond=0)
    #     super().save(*args, **kwargs)


# calendar has a range of days that user can choose to set meeting
class Calendar(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')

    def __str__(self):
        return self.patient.name + " + " + self.doctor.name
    
    def get_calendar_patient(patient):
        return Calendar.objects.get(patient=patient)
    
    def get_all_patient_calendar(doctor):
        return Calendar.objects.filter(doctor=doctor)




class Day(models.Model):
    date = models.DateField()
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, blank=True)
    meeting = models.OneToOneField(Meeting, on_delete=models.CASCADE, blank=True, null=True)

    # def __init__(self, day):
    #     self.date.day = day

    def __str__(self):
        return str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year)
    
    def schedule_meeting(self, meeting):
        self.meeting = meeting
        self.save()
        meeting.save()


def set_days_of_schedule(patient, doctor, date=datetime.date.today()):
    patient_calendar = Calendar(patient=patient, doctor=doctor)
    patient_calendar.save()
    for month in range(date.month, date.month + 3):
        day_num_in_month = calendar.monthrange(date.year, month)[1]
        d_dict = {}
        for day in range(1, day_num_in_month + 1):
            if month > 12:
                d = datetime.date(date.year + 1, month - 12, day)
            d = datetime.date(date.year, month, day)
            d_dict["day{0}".format(day)] = d
            day_obj = Day(date=d, calendar=patient_calendar)
            day_obj.save()
            print(d)

    return patient_calendar.id
        