from django.contrib import admin
from django.urls import path, include
from event.views import organizer_dashboard, participants_dashboard,deleteEvent,updateEvent, createEvent, event_dashboard, eventDetails, rsvp_event


urlpatterns = [
    path("organizer_dashboard/",organizer_dashboard, name='organizer_dashboard'),
    path("participants_dashboard/",participants_dashboard, name='participants_dashboard'),
    path("create-event/",createEvent, name='createEvent'),
    path("update-event/<int:id>/",updateEvent, name='updateEvent'),
    path("delete-event/<int:id>/",deleteEvent, name='deleteEvent'),
    path("show-event/",event_dashboard, name='showEvents'),
    path("event-details/<int:id>",eventDetails, name='eventDetails'),
    path('rsvp/<int:event_id>/', rsvp_event, name='rsvp_event'),
]