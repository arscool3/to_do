# Create your tasks here

from celery import shared_task, Celery
from django.core.mail import send_mail






@shared_task()
def add(x, y):
    return x + y

@shared_task()
def send_email_task(user ):

    send_mail('Дедлайн горит',
              'У тебя горят дедлайны',
              'arslanersain@gmail.com',
              [user.email])




