from django.contrib import admin
from .models import Test, Result, User

# Register your models here.
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(User)