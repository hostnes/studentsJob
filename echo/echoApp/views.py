import hashlib
import json

from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

from .models import Comment, User
from echoApp.forms import AuthForm

from echoApp.models import *
from echoApp.validators import email_validator
from echoApp.backend import get_user, fast_hash, is_user_auth
from echoApp.models import GENDERS


@api_view(["GET"])
def get_countries(request):
    countries = Country.objects.all()
    clean_data = []
    for country in countries:
        country_data = {country.title: []}
        regions = Region.objects.filter(country=country)
        for region in regions:
            region_data = {region.title: []}
            districts = District.objects.filter(region=region)
            for district in districts:
                region_data[region.title].append(district.title)
            country_data[country.title].append(region_data)
        clean_data.append(country_data)
    return JsonResponse({"clean_data": clean_data})


def home(request):
    comments = Comment.objects.all()
    if request.method == 'POST':
        print(request.POST)
        if not 'user' in request.POST :
            if request.POST['text'] != '':
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
                context['error'] = 'This email already in use'
                if not get_user(request.POST['email']):
                    context['error'] = 'Incorrect password'
                    if request.POST['password1'] == request.POST['password2']:
                        user_obj = User.objects.create(email=request.POST['email'], password=fast_hash(request.POST['password1']))
                        session = request.session
                        user = session[settings.USER_SESSION_ID] = {}
                        user['user'] = int(user_obj.id)
                        return redirect('home')
        return render(request, 'echoApp/signup.html', context=context)
    return redirect('home')


def logout(request):
    del request.session['user']
    return redirect('home')


def profile(request):
    if is_user_auth(request):
        context = {}
        countries = Country.objects.all()
        clean_data = []
        for country in countries:
            country_data = {country.title: []}
            regions = Region.objects.filter(country=country)
            for region in regions:
                region_data = {region.title: []}
                districts = District.objects.filter(region=region)
                for district in districts:
                    region_data[region.title].append(district.title)
                country_data[country.title].append(region_data)
            clean_data.append(country_data)
        context['countries'] = clean_data
        if request.method == "GET":
            context['auth_user'] = User.objects.get(id=is_user_auth(request))
            return render(request, 'echoApp/profile.html', context=context)
        elif request.method == "POST":
            user_obj = User.objects.get(email=request.POST['email'])
            try:
                user_obj.img = request.FILES['img']
            except:
                user_obj.img = user_obj.img
            user_obj.first_name = request.POST['first_name']
            user_obj.last_name = request.POST['last_name']
            user_obj.birthday = request.POST['birthday']
            user_obj.gender = request.POST.get('gender')
            user_obj.save()
            context['auth_user'] = user_obj
            return render(request, 'echoApp/profile.html', context=context)
    return redirect('home')


def vacancies(request):
    context = {}
    if is_user_auth(request) != None:
        context['auth_user'] = User.objects.get(id=is_user_auth(request))
    vacancies = Vacancy.objects.all()
    context['vacancies'] = vacancies
    context['experience'] = Experience.objects.all()
    return render(request, 'echoApp/vacancies.html', context=context)


def filter_vacancies(request):
    qwe = request.GET
    print(qwe)
    return HttpResponse({'status': 'ok'})

def vacancy(request, )

# def vacancies(request):
#     context = {'123': 123}
#     return render(request, 'echoApp/vacancies.html', context=context)