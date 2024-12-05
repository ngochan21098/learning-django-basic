from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create_user/', views.create_user, name="create_user"),
    path('update_user/', views.update_user, name="update_user"),
    path('delete_user/', views.delete_user, name="delete_user"),
    path('ticket/create', views.ticket_create, name="ticket_create"),
    path('application/create', views.application_create, name="application_create"),
    path("users/<str:name>/", views.listing_user, name = "listing_user"),
    path("delete/<str:name>/", views.deleting_user, name = "deleting_user"),
    path("member/create/", views.creating_member, name = "creating_member"),
    path("traveller/create/", views.creating_traveller, name = "creating_traveller"),
    path("travellers/<int:traveller_no>/", views.listing_traveller, name = "listing_traveller"),
]
