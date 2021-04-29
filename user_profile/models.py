from django.contrib.auth.models import User
from django.db import models


class MainCycle(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    coinsCount = models.IntegerField(default=0)
    clickPower = models.IntegerField(default=1)
    def Click(self):
        self.coinsCount+=self.clickPower
