from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class MainCycle(models.Model):
    user = models.OneToOneField(User, related_name='cycle', null=False, on_delete=models.CASCADE)
    coinsCount = models.IntegerField(default=0)
    clickPower = models.IntegerField(default=1)
    autoClickPower = models.IntegerField(default=0)
    level = models.IntegerField(default=0)

    def check_level(self):
        if self.coinsCount > (self.level ** 2 + 1) * 1000:
            self.level += 1
            boostType = 1
            if self.level % 3 == 0:
                boostType = 0
            boost = Boost(main_cycle=self, boostType=boostType, level=self.level)
            boost.save()
            self.save()
            return True
        return False


class Boost(models.Model):
    main_cycle = ForeignKey(MainCycle, related_name='boosts', null=False, on_delete=models.CASCADE)
    power = models.IntegerField(default=1)
    level = models.IntegerField(default=0, null=False)
    price = models.IntegerField(default=10)
    boostType = models.IntegerField(default=1)

    def upgrade(self):
        self.main_cycle.coinsCount -= self.price
        if self.boostType == 1:
            self.main_cycle.clickPower += self.power
            self.price *= 5
        else:
            self.main_cycle.autoClickPower += self.power
            self.price *= 10
        self.power *= 2
        self.save()
        self.main_cycle.save()
        return self.main_cycle, self.level, self.price, self.power
