from django.db import models

STRATEGIES = (
    ('5','5min ORB'),
    ('SR','S/R Break'),
    ('EC','10/20 ema cross')
)

# Create your models here.
class Test(models.Model):
    strategy = models.CharField(
        max_length=2,
        choices=STRATEGIES)
    ticker = models.CharField(max_length=4)
    date = models.DateField()

    def __str__(self):
        return f'{self.ticker},{self.date}'

class Result(models.Model):
    PL_percent = models.IntegerField()
    PL_abs = models.IntegerField()
    volume = models.IntegerField()
    entry_price = models.IntegerField()
    exit_price = models.IntegerField()
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test.strategy},{self.PL_percent}'
