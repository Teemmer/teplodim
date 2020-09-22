from threading import Thread
from django.core.mail import send_mail
from django.conf import settings


class EmailThread(Thread):
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message
        Thread.__init__(self)

    def run(self):
        send_mail(self.subject, self.message, settings.EMAIL_HOST_USER, ['dziga2000@gmail.com'])


def send_async_mail(subject, html_content):
    EmailThread(subject, html_content).start()