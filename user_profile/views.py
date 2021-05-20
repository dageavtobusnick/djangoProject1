from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics

from user_profile.serializers import UserSerializer, UserDetailSerializer, CycleSerializer, CycleDetailSerializer
from .models import MainCycle


class UsersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class CycleView(generics.ListCreateAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializer


class CycleDetailView(generics.RetrieveAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleDetailSerializer


def call_click(request):
    main_cycle = MainCycle.objects.filter(user=request.user)[0]
    main_cycle.click()
    main_cycle.save()
    return HttpResponse(main_cycle.coinsCount)
