from django.shortcuts import render, redirect
from django.http import HttpResponse
from event.forms import EventForm, EventDetailsForm
from event.models import Participant, Event
from datetime import date
from django.db.models import Count, Q
from django.contrib import messages

# Create your views here.


def viewEvents(request):
    events = Event.objects.all()
    return render(request, "showEvents.html", {"events": events})


# in views.py
def createEvent(request):
    participants = Participant.objects.all()
    eventForm = EventForm()
    eventDetailsForm=EventDetailsForm()

    if request.method == "POST":
        print("✅ POST:")
        eventForm = EventForm(request.POST)
        eventDetailsForm = EventDetailsForm(request.POST)
        
        if eventForm.is_valid() and eventDetailsForm.is_valid():
            '''for event form'''
            print("I'm in")
            event=eventForm.save()
            eventDetails=eventDetailsForm.save(commit=False)#obj will create but wont be saved in database
            #if we save asa it is, we wont be able to assign event to event details
            eventDetails.event=event
            eventDetails.save()

            messages.success(request,"Event created successfully!")
            return redirect("createEvent")
            
    context = {"eventForm": eventForm,"eventDetailsForm":eventDetailsForm}
    return render(request, "createEvent.html", context)


def updateEvent(request):
    pass


def deleteEvent(request):
    pass


def organizer_dashboard(request):

    tot_participants = Participant.objects.count()
    today = date.today()
    todayEvents = Event.objects.filter(date=today)
    count = Event.objects.aggregate(
        totalEvents=Count("id"),
        todayEvents=Count("id", filter=Q(date=today)),
        pastEvents=Count("id", filter=Q(date__lt=today)),
        upcomingEvents=Count("id", filter=Q(date__gt=today)),
    )

    type=request.GET.get('type','all') 
    #request.GET is a dcitionary which holds infor related to the query

    baseEvents = (
        Event.objects.select_related("category")  # ForeignKey: Category
        .select_related("eventdetails")  # OneToOneField: EventDetails (reverse access)
        .prefetch_related("participants")  # ManyToManyField: Participants
    )

    title="Today"
    #retriving event data
    if type=="past":
        events=baseEvents.filter(date__lt=today)
        title="Past"
    elif type=="upcoming":
        events=baseEvents.filter(date__gt=today)
        title="Upcoming"
    elif type=="ongoing":
        events=baseEvents.filter(date=today)
        title="Today's"
    elif type=="all":
        events=baseEvents.all()
        title=""


    context = {
        "events": events,
        "count": count,
        "tot_participants": tot_participants,
        "title":title,
        "is_organizer": True,
        
    }

    return render(request, "dashboard/organizer_dashboard.html", context)


def participants_dashboard(request):
    tot_participants = Participant.objects.count()
    today = date.today()
    todayEvents = Event.objects.filter(date=today)
    count = Event.objects.aggregate(
        totalEvents=Count("id"),
        todayEvents=Count("id", filter=Q(date=today)),
        pastEvents=Count("id", filter=Q(date__lt=today)),
        upcomingEvents=Count("id", filter=Q(date__gt=today)),
    )

    type=request.GET.get('type','all') 
    #request.GET is a dcitionary which holds infor related to the query

    baseEvents = (
        Event.objects.select_related("category")  # ForeignKey: Category
        .select_related("eventdetails")  # OneToOneField: EventDetails (reverse access)
        .prefetch_related("participants")  # ManyToManyField: Participants
    )

    title="Today"
    #retriving event data
    if type=="past":
        events=baseEvents.filter(date__lt=today)
        title="Past"
    elif type=="upcoming":
        events=baseEvents.filter(date__gt=today)
        title="Upcoming"
    elif type=="ongoing":
        events=baseEvents.filter(date=today)
        title="Today's"
    elif type=="all":
        events=baseEvents.all()
        title=""


    context = {
        "events": events,
        "count": count,
        "tot_participants": tot_participants,
        "title":title,
        "is_organizer": False,
        
    }
    return render(request, "dashboard/participants_dashboard.html",context)


def event_dashboard(request):
    pass
