from django.urls import path

from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]
