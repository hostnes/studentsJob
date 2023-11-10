from django.contrib import admin
from django.urls import path

from echoApp.views import home, login, signup, profile, vacancies, logout

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile'),
    path('vacancies', vacancies, name='vacancies'),
]
