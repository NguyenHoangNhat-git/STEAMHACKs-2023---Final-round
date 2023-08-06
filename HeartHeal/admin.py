from django.contrib import admin

from .models.user import User, Message, Examination
from .models.post import Post
from .models.journal import Note
from .models.schedule import Meeting, Calendar, Day


admin.site.register(Post)

class AdminUser(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'role')

admin.site.register(User, AdminUser)

admin.site.register(Message)
admin.site.register(Note)
admin.site.register(Meeting)
admin.site.register(Calendar)
admin.site.register(Examination)
admin.site.register(Day)
