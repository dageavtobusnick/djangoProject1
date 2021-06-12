from django.contrib.auth.models import User

from user_profile.models import MainCycle, Boost
from user_profile.serializers import BoostDetailSerializer


def main_page(request):
    user = User.objects.filter(id=request.user.id)
    if len(user) > 0:
        main_cycle = MainCycle.objects.filter(user=request.user)[0]
        return False, 'index.html', {'user': user[0], "mainCycle": main_cycle}
    else:
        return True, 'login', {}


def buy_boost(request):
    boost_level = request.data["boost_level"]
    main_cycle = MainCycle.objects.filter(user=request.user)[0]
    boost = Boost.objects.get_or_create(main_cycle=main_cycle, level=boost_level)[0]
    boost.save()
    main_cycle, level, price, power = boost.upgrade()
    return {"click_power": main_cycle.clickPower,
            'auto_click_power': main_cycle.autoClickPower,
            "coins_count": main_cycle.coinsCount,
            "level": level,
            "price": price,
            "power": power,
            "main_cycle": main_cycle.id}


def set_cycle(request):
    user = request.user
    data = request.data
    cycle = MainCycle.objects.filter(user=user)
    cycle.update(coinsCount=data['coinsCount'])
    cycle[0].check_level()
    cycle[0].save()
    boosts = BoostDetailSerializer(Boost.objects.filter(main_cycle=cycle[0]), many=True).data
    return {'success': 'ok', "coinsCount": cycle[0].coinsCount, "boosts": boosts}
