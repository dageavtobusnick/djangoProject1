from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


class MainCycle(models.Model):
    user = models.OneToOneField(User, related_name='cycle', null=False, on_delete=models.CASCADE)
    coinsCount = models.IntegerField(default=0)
    clickPower = models.IntegerField(default=1)
    level = models.IntegerField(default=0)

    def click(self):
        self.coinsCount += self.clickPower


class Boost(models.Model):
    main_cycle = ForeignKey(MainCycle, related_name='boosts', null=False, on_delete=models.CASCADE)
    power = models.IntegerField(default=1)
    level = models.IntegerField(default=0, null=False)
    price = models.IntegerField(default=10)

    def upgrade(self):
        self.main_cycle.clickPower += self.power
        self.power *= 2
        self.main_cycle.coinsCount -= self.price
        self.price *= 2
        self.main_cycle.save()
        self.save()
        return self.main_cycle.clickPower, self.main_cycle.coinsCount, self.level, self.price,self.power
