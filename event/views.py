from django.shortcuts import render
from django.http import HttpResponse
from event.forms import EventForm
from event.models import Participant, Event
from datetime import date
# Create your views here.


def viewEvents(request):
    events = Event.objects.all()
    return render(request, "showEvents.html", {"events": events})


# in views.py
def createEvent(request):
    participants = Participant.objects.all()
    form = EventForm()
    if request.method == "POST":
        print("✅ POST:")
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            context = {"form": form, "message": "Task added successfully!"}
            return render(
                request,
                "createEvent.html",
                context,
            )
    context = {"form": form}
    return render(request, "createEvent.html", context)


def updateEvent(request):
    pass


def deleteEvent(request):
    pass


def organizer_dashboard(request):
    events = Event.objects.all()
    totalEvents = events.count()
    upcoming = Event.objects.filter(status="UP_COMING").count()
    past = Event.objects.filter(status="PAST").count()
    ongoing = Event.objects.filter(status="ON_GOING").count()
    tot_participants=Participant.objects.all().count()
    today = date.today()
    todayEvents=Event.objects.filter(date=today)
    todayEventsCount=todayEvents.count()
    pastEvents=Event.objects.filter(date__lt=today)
    pastEventsCount=pastEvents.count()
    upcomingEvents=Event.objects.filter(date__gt=today)
    upcomingEventsCount=upcomingEvents.count()

    context = {
        "events": events,
        "totalEvents": totalEvents,
        "upcoming": upcoming,
        "past": past,
        "tot_participants":tot_participants,
        "ongoing": ongoing,
        "todayEvents":todayEvents,
        "todayEventsCount":todayEventsCount,
        "pastEvents":pastEvents,
        "pastEventsCount":pastEventsCount,
        "upcomingEvents":upcomingEvents,
        "upcomingEventsCount":upcomingEventsCount,
    }

    return render(request, "dashboard/organizer_dashboard.html", context)


def participants_dashboard(request):
    return render(request, "dashboard/participants_dashboard.html")


def event_dashboard(request):
    pass
