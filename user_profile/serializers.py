from django.contrib.auth.models import User
from rest_framework import serializers

from user_profile.models import MainCycle, Boost


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cycle']


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id']


class CycleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id', 'user', 'coinsCount', 'autoClickPower', 'clickPower', 'boosts']


class BoostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boost
        fields = ['id', "price", 'power', 'level', 'boostType']
