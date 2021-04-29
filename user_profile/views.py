from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics

from user_profile.forms import UserForm
from user_profile.serializers import UserSerializer, UserDetailSerializer, ClickerDataSerializer
from .models import MainCycle


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class ClickView(generics.UpdateAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = ClickerDataSerializer

    def update(self, request, name):
        user = User.objects.filter(username=name)[0]
        cycle = MainCycle.objects.filter(user=user)[0]
        cycle.Click()
        cycle.save()
        return HttpResponse(cycle.coinsCount)


class ClickGetView(generics.UpdateAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = ClickerDataSerializer

    def update(self, request, name):
        user = User.objects.filter(username=name)[0]
        cycle = MainCycle.objects.filter(user=user)[0]
        return HttpResponse(cycle.coinsCount)


def index(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) > 0:
        mainCycle = MainCycle.objects.filter(user=request.user)[0]
        return render(request, 'index.html', {'user': user[0], "mainCycle": mainCycle})
    else:
        return redirect('login')


def click(request):
    return render(request, "clicker.html")


def callClick(request):
    mainCycle = MainCycle.objects.filter(user=request.user)[0]
    mainCycle.Click()
    mainCycle.save()
    return HttpResponse(mainCycle.coinsCount)


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'invalid': True})
    else:
        return render(request, 'login.html', {'invalid': False})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                main_cycle = MainCycle()
                main_cycle.user = user
                main_cycle.save()
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect('index')
            except ValidationError as error:
                return render(request, 'registration.html',
                              {'invalid': True, 'form': form, 'message': error.messages[0]})
        else:
            return render(request, 'registration.html', {'invalid': True, 'form': form, 'message': 'Incorrect Data'})
    else:
        return render(request, 'registration.html', {'invalid': False, 'form': UserForm(), })
