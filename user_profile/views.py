from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

import servises
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
    coins_count = servises.clicker_services.call_click(request)
    return HttpResponse(coins_count)

@api_view(['POST'])
def buy_boost(request):
    params = servises.clicker_services.buy_boost(request)
    return Response(params)
