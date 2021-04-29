from django.contrib.auth.models import User
from rest_framework import serializers

from user_profile.models import MainCycle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ClickerDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MainCycle
        fields = []
