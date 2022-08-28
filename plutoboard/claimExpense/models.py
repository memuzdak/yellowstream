from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField('username', max_length=20, blank=True, null=True)
    password = models.CharField('password', max_length=20, blank=True, null=True)
    email = models.EmailField('email', max_length=20, blank=True, null=True)


class Expense(models.Model):
    name = models.CharField('name', max_length=20, blank=True, null=True)
    description = models.CharField('description', max_length=20, blank=True, null=True)
    amount = models.IntegerField('amount', max_length=4, blank=True, null=True)
    file = models.FileField('file', blank=True, null=True)