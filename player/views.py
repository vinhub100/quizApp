from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Player


def home(request):
    if request.user.is_authenticated():
        player = Player.objects.get(user=request.user)
        return render(request, 'player/user_home.html', {'player': player})
    else:
        return render(request, 'player/home.html')


def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if not form.is_valid():
                return render(request, 'player/signup.html', {'form': form})

            else:
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                User.objects.create_user(username=username, password=password, email=email)
                user = authenticate(username=username, password=password)
                Player.objects.create(user=user)
                login(request, user)
                return redirect('home')

        else:
            return render(request, 'player/signup.html', {'form': SignUpForm()})


def signin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect('/signup')
            else:
                return HttpResponseRedirect('/signup')
        else:
            return render(request, 'player/login.html')

