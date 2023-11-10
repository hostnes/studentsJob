import hashlib

from django.conf import settings
from django.shortcuts import render, redirect
from .models import Comment, User
from echoApp.forms import AuthForm

from echoApp.models import User
from echoApp.validators import email_validator
from echoApp.backend import get_user, fast_hash, is_user_auth


def home(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        print(request.POST)
        if not 'user' in request.POST and request.POST['text'] != '':
            session = request.session
            user = session.get(settings.USER_SESSION_ID)
            user_obj = User.objects.get(id=user['user'])
            Comment.objects.create(user=f'{user_obj.first_name} {user_obj.last_name}', text=request.POST['text'], photo=user_obj.img)
        elif request.POST['user'] != '' and request.POST['text'] != '':
            Comment.objects.create(user=request.POST['user'], text=request.POST['text'])
    context = {
        'comments': comments
    }
    if is_user_auth(request) != None:
        context['auth_user'] = User.objects.get(id=is_user_auth(request))
    return render(request, 'echoApp/home.html', context=context)


def login(request):
    if not is_user_auth(request):
        context = {}
        if request.method == "POST":
            context['error'] = 'Email is invalid'
            if email_validator(request.POST['email']) == True:
                context['error'] = 'This email does not exist'
                if get_user(request.POST['email']):
                    context['error'] = 'Incorrect password'
                    user_obj = User.objects.filter(email=request.POST['email'], password=fast_hash(request.POST['password']))
                    if len(user_obj) == 1:
                        session = request.session
                        user = session[settings.USER_SESSION_ID] = {}
                        user['user'] = user_obj[0].id
                        return redirect('home')
        return render(request, 'echoApp/login.html', context=context)
    return redirect('home')


def signup(request):
    if not is_user_auth(request):
        context = {}
        if request.method == "POST":
            context['error'] = 'Email is invalid'
            if email_validator(request.POST['email']) == True:
                context['error'] = 'This email does not exist'
                if get_user(request.POST['email']):
                    context['error'] = 'Incorrect password'
                    if request.POST['password1'] == request.POST['password2']:
                        user_obj = User.objects.create(email=request.POST['email'], password=fast_hash(request.POST['password1']))
                        session = request.session
                        user = session.get(settings.USER_SESSION_ID)
                        user['user'] = user_obj.id
                        return redirect('home')
        return render(request, 'echoApp/signup.html', context=context)
    return redirect('home')


def logout(request):
    del request.session['user']
    return redirect('home')


def profile(request):
    return render(request, 'echoApp/profile.html')


def vacancies(request):
    return render(request, 'echoApp/vacancies.html')