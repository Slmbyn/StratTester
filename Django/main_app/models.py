from django.db import models
from django.contrib.auth.models import User

STRATEGIES = [
    ('5min ORB', '5min ORB'),
    ('S/R Break','S/R Break'),
    ('10/20 ema cross','10/20 ema cross')
]

# Create your models here.
class Test(models.Model):
    strategy = models.CharField(
        max_length=200,
        choices=STRATEGIES)
    ticker = models.CharField(max_length=4)
    date = models.DateField()

    def __str__(self):
        return f'{self.ticker},{self.date}'

class Result(models.Model):
    PL_percent = models.DecimalField(max_digits=10, decimal_places=4)
    PL_abs = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    entry_price = models.DecimalField(max_digits=10, decimal_places=2)
    exit_price = models.DecimalField(max_digits=10, decimal_places=2)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test.strategy},{self.PL_percent}'
