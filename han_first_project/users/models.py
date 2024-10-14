from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    salary = models.BigIntegerField()
    hometown = models.CharField(max_length=20)


class Application(models.Model):
    apl_no = models.CharField(max_length=20)
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)


class Reservation(models.Model):
    ref_no = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    fit_id = models.CharField(max_length=20)
