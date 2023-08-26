from django.shortcuts import render, redirect
from django.views import View

from HeartHeal.models.user import User
from HeartHeal.models.task import Goal, Task, get_all_goals

import datetime

class Goal_me(View):

    def get(self, request):
        if ('user' not in request.session):
            return redirect('login')
        
        current_user = User.get_user_by_id(request.session['user'])
        if request.session['role'] == 'doctor':
            return redirect('dashboard')

        long_term_goals = get_all_goals(current_user, 'long_term')
        short_term_goals = get_all_goals(current_user, 'short_term')
        today = datetime.date.today()

        data ={
            "long_term": long_term_goals,
            "short_term": short_term_goals,
            'current_user': current_user,
            'today' : today
        }
        return render(request, "task.html", data)
    
    def post(self, request):
        current_user = User.get_user_by_id(request.session['user'])
        if 'task' in request.POST:
            checked_tasks = request.POST.getlist('task')
            if checked_tasks:
                for checked_task_id in checked_tasks:
                    task = Task.objects.get(id=checked_task_id)
                    task.done = True
                    task.save()
        elif 'add_goal_title' in request.POST:
            task_inputs = request.POST.getlist("add_task")

            new_goal = Goal(title=request.POST['add_goal_title'], patient=current_user, type=request.POST['add-goal-type'])
            new_goal.save()

            for task_content in task_inputs:
                Task.objects.create(content=task_content, goal=new_goal)
            new_goal.save()

        return redirect('goal')