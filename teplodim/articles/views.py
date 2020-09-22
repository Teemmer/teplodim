from django.shortcuts import render
from django.views import View

from .helper import send_async_mail
from .models import Article


class HomeView(View):
    template_name = 'articles_template.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'articles': Article.objects.all()})


class ContactView(View):
    template_name = 'contact_template.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'articles': Article.objects.all()})

    def post(self, request, *args, **kwargs):
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_async_mail(subject, message)
        return render(request, self.template_name, {'sent': True})


class AboutView(View):
    template_name = 'articles_template.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {'articles': Article.objects.all()})
