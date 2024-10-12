from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    age = models.SmallIntegerField()
    salary = models.BigIntegerField()
    hometown = models.CharField(max_length=20)

class Application(models.Model):
    apl_no = models.SmallIntegerField(primary_key=True) 
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)

class Member(models.Model):
    mem_no = models.BigIntegerField(primary_key = True)    

class Traveller(models.Model): 
    traveller_no = models.SmallIntegerField(primary_key = True)
    mem_no = models.ForeignKey('users.Member', on_delete=models.DO_NOTHING)
    apl_no = models.ForeignKey('users.Application', on_delete=models.DO_NOTHING)
    mem_status = models.BooleanField()
    mem_name = models.CharField(max_length = 20)
    mem_birth = models.DateTimeField()

class Ticket(models.Model):
    ticket_no = models.SmallIntegerField(primary_key = True)
    apl_no = models.ForeignKey('users.Application', on_delete=models.DO_NOTHING)

## Test




     