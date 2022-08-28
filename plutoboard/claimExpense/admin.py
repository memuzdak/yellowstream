from django.contrib import admin


from .models import User
from .models import Expense
# Register your models here.

admin.register(User, Expense)(admin.ModelAdmin)

