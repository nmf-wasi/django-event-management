from django.db.models.signals import (
    post_delete,
    post_init,
    pre_delete,
    pre_init,
    m2m_changed,
    post_save
)
from django.dispatch import receiver
from django.core.mail import send_mail
from event.models import Participant, Category, Event, EventDetails
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth.models import User, Group

@receiver(post_save, sender=User)
def sendActivaionEMail(sender, instance,created, **kwargs):
    if created and getattr(instance, '_send_activation', False):
        token=default_token_generator.make_token(instance)
        activation_url=f"{settings.FRONT_END_URL}/participants/activate/{instance.id}/{token}/"
        subject="Activate your account"
        message=f"Hi {instance.username},\n\nPlease activate your account by cliciking the link below:\n\n{activation_url}\n\nThank you"
        recipient_list=[instance.email]
        try:
            send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)
        except Exception as e:
            print(f"Failed to send email to {instance.email}: {str(e)}")


@receiver(post_save, sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        userGroup, created=Group.objects.get_or_create(name='User')
        instance.groups.add(userGroup)
        instance.save()