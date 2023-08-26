from django.contrib import admin

from .models.user import User, Message, Examination
from .models.journal import Note
from .models.schedule import Meeting, Calendar, Day
from .models.task import Goal, Task
from .models.post import Post, Comment, Like, Category
from .models.practice import Practice_Category, Practice, Module, Module_user, What_yll_learn
from .models.news import News, News_Category, News_Comments


class AdminUser(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'role')

admin.site.register(User, AdminUser)
admin.site.register(Examination) 

admin.site.register(Message)

admin.site.register(Note)

admin.site.register(Meeting)
admin.site.register(Calendar)
admin.site.register(Day)

admin.site.register(Goal)
admin.site.register(Task)

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)

admin.site.register(Practice)
admin.site.register(Practice_Category)
admin.site.register(Module)
admin.site.register(Module_user)
admin.site.register(What_yll_learn)

admin.site.register(News)
admin.site.register(News_Category)
admin.site.register(News_Comments)