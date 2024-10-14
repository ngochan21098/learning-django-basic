from django.shortcuts import render
from django.http import HttpResponse
from .models import Ticket 

# Create your views here.

def create_user(req):
    return HttpResponse('OK')

def ticket_create(req):
    return HttpResponse('OK')