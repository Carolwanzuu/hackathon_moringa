from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from decouple import config

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the Y-Chama'
    sender = config('EMAIL_HOST_USER')

    #passing in the context vairables
    text_content = render_to_string('email/inviteemail.txt',{"name": name})
    html_content = render_to_string('email/inviteemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()