from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views.home import home, home_me
from .views.login import Login
from .views.signup import Signup

from .views.dashboard import Dashboard, remove_therapist
from .views.journal import Journal
from .views.schedule import Schedule, Schedule_me
from .views.goal_me import Goal_me
from .views.practice import Practice_home
from .views.practice_detail import Practice_detail, Practice_start
from .views.chat import chat_rooms, chat_room_user
from .views.forum import Forum

from .views.info import hotlines, how_it_works, about, contact, news, detail

urlpatterns = [
    path('', home, name='home'),
    path('home-me', home_me, name='home-me'),
    path('login', Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),

    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('remove-therapist/<int:user_id>', remove_therapist, name='remove-therapist'),

    path('chat-room', chat_rooms.as_view(), name='chat-room'),
    path('chat-room/<str:room_name>', chat_room_user, name='chat-room'),

    path('journal', Journal.as_view(), name='journal'),

    path('goal', Goal_me.as_view(), name='goal'),
    
    path('practice-home', Practice_home.as_view(), name='practice-home'),
    path('practice-detail/<int:practice_id>', Practice_detail.as_view(), name='practice-detail'),
    path('practice-start/<int:practice_id>', Practice_start.as_view(), name='practice-start'),
    path('practice-start/<int:practice_id>/<int:module_id>', Practice_start.as_view(), name='practice-start'),

    path('schedule', Schedule.as_view(), name='schedule'),
    path('schedule-me', Schedule_me.as_view(), name='schedule-me'),

    path('forum', Forum.as_view(), name='forum'),
    path('forum/<str:category>', Forum.as_view(), name='forum'),

    # INFO
    path('hotlines', hotlines, name='hotlines'),
    path('how-it-works', how_it_works, name='how-it-works'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('news', news, name='news'),
    path('detail/<int:post_id>', detail, name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
