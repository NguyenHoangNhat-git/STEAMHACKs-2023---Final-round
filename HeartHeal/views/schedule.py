from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View
from django.db.models import Q

from HeartHeal.models.schedule import Meeting, set_days_of_schedule, Calendar, Day
from HeartHeal.models.user import User

import datetime 

def divide_month(days):
    previous_month = []
    current_month = []
    next_month = []
    for day in days:
        if day.date.month == days[0].date.month:
            previous_month.append(day)
        elif day.date.month == days[0].date.month + 1:
            current_month.append(day)
        elif day.date.month == days[0].date.month + 2:
            next_month.append(day)
    months = []
    months.extend([previous_month, current_month, next_month])
    return months

def schedule_me(request):
    if ('user' not in request.session):
        return redirect('login')
    calendar = Calendar.objects.filter(patient=request.session['user'])[0]
    days = Day.objects.filter(calendar=calendar)
    days_have_meeting = []
    for day in days:
        if day.meeting:
            print("have meeting")
            days_have_meeting.append(day)

    data = {
        "days" : days_have_meeting
    }
    return render(request, 'schedule_me.html', data)

class Schedule(View):
    current_month = False
    error = ""

    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        calendar = Calendar.objects.filter(patient=request.session['user'])
        if not calendar:
            current_patient = User.objects.filter(id=request.session['user'])[0]
            calendar_id = set_days_of_schedule(current_patient, current_patient.assigned_doctor)
            calendar = Calendar.objects.filter(id=calendar_id)
        days = Day.objects.filter(calendar=calendar[0])

        # filter days of each month
        months = divide_month(days)
        data={
            'months' : months, 
            'error': ""
            }
        return render(request, "schedule.html", data)
    
    def post(self, request):
        current_user = User.objects.filter(id=request.session['user'])[0]

        if "ngay" not in request.POST:
            self.error = "Vui lòng chọn ngày"
        elif "gio" not in request.POST: 
            self.error = "Vui lòng chọn giờ"
        elif "bao_lau" not in request.POST:
            self.error = "Vui lòng chọn giới hạn thời gian"
        else:
            day_month_year = request.POST['ngay'].split('/')
            date = datetime.date(day=int(day_month_year[0]), month=int(day_month_year[1]), year=int(day_month_year[2]))
            day_of_meeting = Day.objects.filter(date=date)[0]
            minute = int(request.POST['bao_lau'])
            when = int(request.POST['gio'])

            duration =  datetime.timedelta(seconds=minute*60)

            new_meeting = Meeting(title="Cuộc họp của "+current_user.name+" + "+current_user.assigned_doctor.name+" ngày "+request.POST['ngay'], duration=duration, when=when)
            new_meeting.save()
            day_of_meeting.schedule_meeting(meeting=new_meeting)

            
        return redirect('schedule')


