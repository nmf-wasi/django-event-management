from django.db import models


# Create your models here.


class Participant(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    STATUS_CHOICES = [
        ("ON_GOING", "On Going"),
        ("PAST", "Past"),
        ("UP_COMING", "Up Coming"),
    ]
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default="UP_COMING"
    )
    is_completed = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        default="None",
        on_delete=models.SET_NULL,
        related_name="events",
        null=True,
        blank=True,
    )
    participants = models.ManyToManyField(Participant, related_name="events")



class EventDetails(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    notes = models.TextField(max_length=500, blank=True, null=True)
    livestream_url = models.TextField(blank=True, null=True)
    speakers = models.TextField(blank=True, null=True)
