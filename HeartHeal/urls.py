from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views.home import home
from .views.login import Login
from .views.signup import Signup
from .views.dashboard import Dashboard
from .views.chat import Chat
from .views.journal import Journal
from .views.schedule import Schedule, schedule_me

urlpatterns = [
    path('', home, name='home'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),

    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('chat', Chat.as_view(), name='chat'),

    path('journal', Journal.as_view(), name='journal'),

    path('schedule', Schedule.as_view(), name='schedule'),
    path('schedule-me', schedule_me, name='schedule-me'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
