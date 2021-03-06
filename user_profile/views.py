from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

import servises
from user_profile.serializers import UserSerializer, UserDetailSerializer, CycleSerializer, CycleDetailSerializer, \
    BoostDetailSerializer
from .models import MainCycle, Boost


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class CycleView(generics.ListAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializer


class CycleDetailView(generics.RetrieveAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleDetailSerializer


class BoostListView(generics.ListAPIView):
    queryset = Boost.objects.all()
    serializer_class = BoostDetailSerializer

    def get_queryset(self):
        return Boost.objects.filter(main_cycle=self.kwargs['mainCycle'])


@api_view(['POST'])
def buy_boost(request):
    params = servises.clicker_services.buy_boost(request)
    return Response(params)


@api_view(['POST'])
def set_main_cycle(request):
    params = servises.clicker_services.set_cycle(request)
    return Response(params)
