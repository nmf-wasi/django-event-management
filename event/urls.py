from django.contrib import admin
from django.urls import path, include
from event.views import organizer_dashboard, participants_dashboard, createEvent, viewEvents


urlpatterns = [
    path("organizer_dashboard/",organizer_dashboard, name='organizer_dashboard'),
    path("participants_dashboard/",participants_dashboard, name='participants_dashboard'),
    path("create-event/",createEvent, name='createEvent'),
    path("show-event/",viewEvents, name='viewEvents'),
]