from django.contrib import admin
from event.views import Event, EventDetails, Participant, Category
# Register your models here.
admin.site.register(Event)
admin.site.register(EventDetails)
admin.site.register(Participant)
admin.site.register(Category)