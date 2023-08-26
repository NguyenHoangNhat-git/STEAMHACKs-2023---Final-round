from django.shortcuts import render, redirect

from django.views import View

from HeartHeal.models.schedule import Meeting, set_days_of_schedule, Calendar, Day
from HeartHeal.models.user import User

import datetime 

def divide_month(days):
    current_month = []
    next_month = []
    next2_month = []
    for day in days:
        if day.date.month == days[0].date.month:
            current_month.append(day)
        elif day.date.month == days[0].date.month + 1:
            next_month.append(day)
        elif day.date.month == days[0].date.month + 2:
            next2_month.append(day)
    months = []
    months.extend([current_month, next_month, next2_month])
    return months

def get_meeting_days_in_calendar(calendar):
    days = Day.objects.filter(calendar=calendar)
    days_have_meeting = []
    for day in days:
        if day.meeting:
            days_have_meeting.append(day)
    return days_have_meeting

class Schedule_me(View):
    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        current_user = User.get_user_by_id(request.session['user'])
        
        if request.session['role'] == 'doctor':
            calendars = Calendar.get_all_patient_calendar(doctor=current_user)
            days_have_meeting = []
            for calendar in calendars:
                days_have_meeting_per_patient = get_meeting_days_in_calendar(calendar)
                days_have_meeting += days_have_meeting_per_patient
        
        else:
            calendar = Calendar.get_calendar_patient(patient=current_user)
            if not calendar:
                return redirect('schedule')
            days_have_meeting = get_meeting_days_in_calendar(calendar)

        data = {
            "days" : days_have_meeting,
            'current_user': current_user
        }
        return render(request, 'schedule_me.html', data)
    
    def post(self, request):
        if 'meeting_link' in request.POST:
            meeting = Meeting.objects.get(id=request.POST['meeting_id'])
            meeting.link_meeting = request.POST['meeting_link']
            meeting.save()
        elif 'cancel_meeting' in request.POST:
            meeting = Meeting.objects.get(id=request.POST['meeting_id'])
            print('deleting')
            meeting.delete()
        return redirect('schedule-me')



class Schedule(View):
    current_month = False
    error = ""

    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        current_user = User.get_user_by_id(request.session['user'])

        if request.session['role'] == 'doctor':
            return redirect('schedule-me')

        calendar = Calendar.objects.filter(patient=current_user)
        if not calendar:
            calendar_id = set_days_of_schedule(current_user, current_user.assigned_doctor)
            calendar = Calendar.objects.filter(id=calendar_id)
        days = Day.objects.filter(calendar=calendar[0])

        # filter days of each month
        months = divide_month(days)
        data={
            'months' : months, 
            'error': "",
            'current_user': current_user
            }
        return render(request, "schedule.html", data)
    
    def post(self, request):
        current_user = User.get_user_by_id(request.session['user'])

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


