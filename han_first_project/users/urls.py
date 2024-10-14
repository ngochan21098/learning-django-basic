from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name="create_user"),
    path('ticket/create', views.ticket_create, name="ticket_create"),
]