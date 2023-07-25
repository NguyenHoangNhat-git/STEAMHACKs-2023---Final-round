from django.contrib import admin

from .models.user import User
from .models.post import Post


# Category
admin.site.register(Post)


# Products
class AdminUser(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

admin.site.register(User, AdminUser)