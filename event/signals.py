from django.dispatch import receiver
from django.core.mail import send_mail
from event.models import Participant, Category, Event, EventDetails
from django.conf import settings
from django.db.models.signals import m2m_changed


@receiver(m2m_changed,sender=Event.assigned_to.through)
def notifyEmployeesOnTaskCreation(sender, instance, action, **kwargs):
    if action=='post_add':
        print(instance, instance.assigned_to.all())
        assigned_emails=[emp.email for emp in instance.assigned_to.all()]
        print("Checking",assigned_emails)
        send_mail(
            "New Event scheduled!",
            f"You have been assigned to {instance.name}.",
            "nmfairuz12@gmail.com",
            assigned_emails,
            fail_silently=False,
        )
