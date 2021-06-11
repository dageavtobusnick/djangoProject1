from django.contrib.auth.models import User
from rest_framework.decorators import api_view

from user_profile.models import MainCycle, Boost
from user_profile.serializers import BoostDetailSerializer


def main_page(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) > 0:
        main_cycle = MainCycle.objects.filter(user=request.user)[0]
        return False, 'index.html', {'user': user[0], "mainCycle": main_cycle}
    else:
        return True, 'login', {}


def call_click(request):
    main_cycle = MainCycle.objects.filter(user=request.user)[0]
    main_cycle.click()
    main_cycle.save()
    return main_cycle.coinsCount


def buy_boost(request):
    boost_level = request.data["boost_level"]
    main_cycle = MainCycle.objects.filter(user=request.user)[0]
    boost = Boost.objects.get_or_create(main_cycle=main_cycle, level=boost_level)[0]
    boost.save()
    click_power,coins_count,level,price,power = boost.upgrade()
    return {"click_power":click_power,"coins_count":coins_count,"level":level,"price":price,"power":power}


def call_click(request):
    main_cycle = MainCycle.objects.filter(user=request.user)[0]
    is_level_up=main_cycle.click()
    main_cycle.save()
    if is_level_up:
        boosts =BoostDetailSerializer(Boost.objects.filter(main_cycle=main_cycle),many=True).data
        return {"coinsCount":main_cycle.coinsCount,"boosts":boosts}
    else:
        return {"coinsCount":main_cycle.coinsCount,"boost":None}
