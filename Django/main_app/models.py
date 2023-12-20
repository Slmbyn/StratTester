from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test.strategy},{self.PL_percent}'

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username,password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email