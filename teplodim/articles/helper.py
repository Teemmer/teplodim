from threading import Thread
from django.core.mail import send_mail
from django.conf import settings


params_list = ['f_name', 'l_name', 'phone', 'email',
               'street', 'house', 'flat']


class EmailThread(Thread):
    def __init__(self, subject, message):
        self.subject = subject
        self.message = message
        Thread.__init__(self)

    def run(self):
        send_mail(self.subject, self.message, settings.EMAIL_HOST_USER, ['dziga2000@gmail.com'])


def send_async_mail(subject, message, parameters):
    message_add = ''
    if parameters.get('l_name'):
        message_add += "Прізвище: " + parameters.get('l_name') + '\n'
    if parameters.get('f_name'):
        message_add += "Ім'я: " + parameters.get('f_name') + '\n'
    if parameters.get('phone'):
        message_add += "Телефон: " + parameters.get('phone') + '\n'
    if parameters.get('email'):
        message_add += "Пошта: " + parameters.get('email') + '\n'
    if parameters.get('street'):
        message_add += "Вулиця: " + parameters.get('street') + '\n'
    if parameters.get('house'):
        message_add += "Будинок: " + parameters.get('house') + '\n'
    if parameters.get('flat'):
        message_add += "Квартира: " + parameters.get('flat') + '\n'
    message_add += "Повідомлення: " + message
    EmailThread(subject, message_add).start()
