from django.db import models
from .user import User

ROLE = [
    ('long_term', 'long_term'),
    ('short_term', 'short_term')
]


class Goal(models.Model):
    title = models.TextField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=ROLE, default='short_term')
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def complete(self):
        self.done = True
        self.save()

class Task(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    content = models.TextField()
    # timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    def complete(self):
        self.done = True
        self.save()


def get_all_goals(patient, type):
    return Goal.objects.filter(patient=patient).filter(type=type)

def get_progress_value_func(self):
    tasks = Task.objects.filter(goal=self)
    completed_tasks = tasks.filter(done=True)
    if tasks:
        return int(( completed_tasks.count() / tasks.count() ) * 100 )
    else:
        if self.done == True:
            return int(100)
        else:
            return int(0)
        
def get_all_tasks_func(self):
    tasks = Task.objects.filter(goal=self)
    if tasks:
        return tasks
    else:
        return False

Goal.get_progress_value = get_progress_value_func
Goal.get_all_tasks = get_all_tasks_func